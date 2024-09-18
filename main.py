from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from typing import Dict, List, Any

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATABASE = "playlistSample.db"

def get_all_tables(conn: sqlite3.Connection) -> List[str]:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def get_table_data(conn: sqlite3.Connection, table: str) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table};")
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error as e:
        print(f"Error fetching data from table {table}: {e}")
        return []

@app.get("/")
async def root():
    return RedirectResponse(url="/get_html_data")

@app.get("/get_json_data")
async def get_json_data():
    try:
        conn = sqlite3.connect(DATABASE)
        tables = get_all_tables(conn)
        if not tables:
            raise HTTPException(status_code=404, detail="No tables found in the database.")

        data = {}
        for table in tables:
            table_data = get_table_data(conn, table)
            data[table] = table_data

        return JSONResponse(content=data)

    except Exception as e:
        print(f"Error: {e}")  # Log the error to console
        raise HTTPException(status_code=500, detail="An internal error occurred.")
    finally:
        conn.close()

@app.get("/get_html_data")
async def get_html_data(request: Request):
    try:
        conn = sqlite3.connect(DATABASE)
        tables = get_all_tables(conn)
        if not tables:
            raise HTTPException(status_code=404, detail="No tables found in the database.")

        data = {}
        for table in tables:
            table_data = get_table_data(conn, table)
            data[table] = table_data

        return templates.TemplateResponse("data_display.html", {"request": request, "data": data})

    except Exception as e:
        print(f"Error: {e}")  # Log the error to console
        raise HTTPException(status_code=500, detail="An internal error occurred.")
    finally:
        conn.close()

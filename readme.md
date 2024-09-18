# FastAPI Data Viewer

This FastAPI application retrieves data from a SQLite database and provides a web interface for viewing it in both HTML and JSON formats. You can easily switch between a tabular HTML view and raw JSON data. Additionally, the application is deployed and accessible at https://project-data-test.onrender.com/get_html_data.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up a Virtual Environment (Recommended)](#2-set-up-a-virtual-environment-recommended)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Prepare the SQLite Database](#4-prepare-the-sqlite-database)
- [Running the Application Locally](#running-the-application-locally)
  - [1. Start the FastAPI Server](#1-start-the-fastapi-server)
  - [2. Access the Application](#2-access-the-application)
- [Accessing the Application](#accessing-the-application)
  - [1. HTML Data View](#1-html-data-view)
  - [2. JSON Data View](#2-json-data-view)
  - [3. Root URL](#3-root-url)
- [License](#license)

## Features

- **SQLite Database Integration**: Connects to a SQLite database (`playlistSample.db`) to fetch and display data.
- **HTML and JSON Views**: Allows users to toggle between viewing data in a structured HTML table or as raw JSON.
- **Dynamic Data Fetching**: Fetches data dynamically from the backend using FastAPI endpoints.
- **Templating with Jinja2**: Uses Jinja2 templates for rendering HTML pages.
- **Deployment Ready**: Easily deployable to platforms like Render with a live demo available.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux
- **Python**: Python 3.8 or higher installed (download from [python.org](https://www.python.org/))
- **Git**: Git installed for version control (download from [git-scm.com](https://git-scm.com/))
- **Virtual Environment** (Recommended): To manage project dependencies (optional)

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/R3ramya/project_data_test.git
cd project_data_test
```

### 2. Set Up a Virtual Environment (Recommended)

It's recommended to use a virtual environment to manage dependencies. You can create one using `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

- Windows:
  ```
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes necessary packages like:

```
fastapi==0.95.1
uvicorn==0.22.0
jinja2==3.1.2
```

If `requirements.txt` is not present, you can generate it using:

```bash
pip freeze > requirements.txt
```

### 4. Prepare the SQLite Database

Ensure the SQLite database file `playlistSample.db` is located in the project's root directory. If you need to create or modify the database, use SQLite tools or scripts.

## Running the Application Locally

To run the FastAPI application on your local machine, follow these steps:

### 1. Start the FastAPI Server

Use uvicorn to run the application:

```bash
uvicorn main:app --reload
```

- `main`: The name of your Python file (without the .py extension).
- `app`: The FastAPI instance in your `main.py`.
- `--reload`: Enables auto-reloading of the server on code changes (useful during development).

### 2. Access the Application

Open your web browser and navigate to:

- HTML Data View: http://127.0.0.1:8000/get_html_data
- JSON Data View: http://127.0.0.1:8000/get_json_data
- Root URL: http://127.0.0.1:8000/

## Accessing the Application

### 1. HTML Data View

- URL: `/get_html_data`
- Description: Displays the data in a formatted HTML table.

### 2. JSON Data View

- URL: `/get_json_data`
- Description: Returns the raw JSON data.

### 3. Root URL

- URL: `/`
- Description: Provides links to both HTML and JSON views.

## License

[MIT License](https://opensource.org/licenses/MIT)

Copyright (c) [year] [fullname]

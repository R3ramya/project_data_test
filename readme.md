# FastAPI Data Viewer

This FastAPI application serves data from a SQLite database and provides a web interface to view the data in both HTML and JSON formats. You can easily toggle between viewing the data in a tabular format or as raw JSON. Additionally, the application is deployed and accessible via [https://project-data-test.onrender.com/get_html_data](https://project-data-test.onrender.com/get_html_data).

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Prepare the SQLite Database](#4-prepare-the-sqlite-database)
- [Directory Structure Example](#directory-structure-example)
- [Running the Application Locally](#running-the-application-locally)
  - [1. Start the FastAPI Server](#1-start-the-fastapi-server)
  - [2. Access the Application](#2-access-the-application)
- [Accessing the Application](#accessing-the-application)
  - [1. HTML Data View](#1-html-data-view)
  - [2. JSON Data View](#2-json-data-view)
  - [3. Root URL](#3-root-url)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

## Features

- **SQLite Database Integration**: Connects to a SQLite database (`playlistSample.db`) to fetch and display data.
- **HTML and JSON Views**: Allows users to toggle between viewing data in a structured HTML table or as raw JSON.
- **Dynamic Data Fetching**: Fetches data dynamically from the backend using FastAPI endpoints.
- **Templating with Jinja2**: Uses Jinja2 templates for rendering HTML pages.
- **Deployment Ready**: Easily deployable to platforms like Render with a live demo available.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux
- **Python**: Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Git installed for version control. Download from [git-scm.com](https://git-scm.com/downloads).
- **Virtual Environment (Recommended)**: To manage project dependencies.

## Installation

Follow these steps to set up and run the application on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/R3ramya/project_data_test.git
cd your-repo

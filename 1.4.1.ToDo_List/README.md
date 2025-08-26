# 📝 To-Do App API with FastAPI and SQLite

This is a simple **To-Do application API** built using **FastAPI** and **SQLite**.

- **FastAPI** handles the API endpoints and HTTP requests.
- **SQLite** is used as the local database for storing tasks.
- The project consists of **two Python files**:
  - `main.py`: defines the API routes
  - `database.py`: handles all database operations

---

## 💾 Requirements

Install dependencies:

```bash
pip install fastapi uvicorn

---

🚀 How to Run

Run the server with:

uvicorn main:app --reload

> Replace main with your actual Python file name if it's different.

Open your browser to:

👉 http://127.0.0.1:8000 — basic welcome

👉 http://127.0.0.1:8000/docs — interactive Swagger UI

---

🧠 Database Info

The app uses SQLite and will automatically create a database file todo.db with a tasks table if it doesn't exist.

Task Table Structure

Column Type Description

id INTEGER Primary key, auto-incremented
title TEXT Title of the task
description TEXT Description of the task
time TEXT Time or deadline as string
status BOOLEAN Task done or not (default: false)

---

🗃️ API Endpoints

---

GET /

Returns a welcome message.

Response:

{"message": "Welcome to the To-Do App"}

---

GET /tasks

Returns all tasks sorted by status.

---

POST /tasks

Add a new task.

Form Data:

title (string) – Required

description (string) – Required

time (string) – Required

---

PUT /tasks

Toggle the task’s status (done ↔ not done).

Form Data:

task_id (integer) – Required

---

DELETE /tasks

Delete a task by its ID.

Form Data:

task_id (integer) – Required

---

🧪 Testing

You can test this API using:

Swagger UI: http://127.0.0.1:8000/docs

Postman

curl


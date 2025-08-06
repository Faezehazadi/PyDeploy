# 📝 To-Do App API with FastAPI and SQLite

This is a simple To-Do application built using **FastAPI** for the backend API and **SQLite** for local data storage. You can create, read, update, and delete tasks using HTTP requests.

---


## ⚙️ Features

- Create a new task with a title, description, and time
- View all tasks
- Update task status (done/not done)
- Delete a task
- View task details by ID

---

## 💾 Requirements

Install dependencies:

```bash
pip install fastapi uvicorn
🚀 How to Run
Run the API server:

uvicorn main:app --reload
> Replace main with your actual Python file name if it's different.
The API will be available at:
👉 http://127.0.0.1:8000

You can also open the Swagger UI for testing: 👉 http://127.0.0.1:8000/docs

🗃️ API Endpoints
GET /
Returns a welcome message.

GET /tasks
Returns the list of all tasks, ordered by completion status.

POST /tasks
Create a new task.

PUT /tasks
Toggle the task status (done/undone).

DELETE /tasks
Delete a task by ID.


🧪 Testing the API
Use curl, Postman, or Swagger UI (/docs) to test the endpoints.

---
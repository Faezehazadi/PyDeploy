from fastapi import FastAPI, Form, HTTPException
from database import Database

app = FastAPI()
db = Database()

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do App"}

@app.get("/tasks")
def read_tasks():
    return db.load_tasks()

@app.post("/tasks")
def create_task(
    title: str = Form(...),
    description: str = Form(...),
    time: str = Form(...)
):
    db.insert_task(title, description, time)
    return {"message": "Task added successfully"}

@app.put("/tasks")
def update_task_status(task_id: int = Form(...)):
    task = db.show_description(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.edit_task_done(task_id)
    return {"message": "Task status updated"}

@app.delete("/tasks")
def delete_task(task_id: int = Form(...)):
    task = db.show_description(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete_task(task_id)
    return {"message": "Task deleted successfully"}


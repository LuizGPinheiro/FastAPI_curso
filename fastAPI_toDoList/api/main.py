from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Habilitar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",  # Adicione a porta que seu servidor está usando para o front-end
    # Adicione outras origens se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool = False

tasks: List[Task] = []
next_id: int = 1

# Criar uma nova tarefa
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = Task(id=next_id, title=task.title, description=task.description, done=False)
    next_id += 1
    tasks.append(new_task)
    return new_task

# Obter a lista de todas as tarefas
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Obter uma tarefa específica
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Atualizar uma tarefa da lista
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    task.done = updated_task.done
    return task

# Exclui uma tarefa da lista
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return

# Agora vamos fazer a execução do servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
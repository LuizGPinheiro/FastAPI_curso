from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Task(BaseModel):
    id:int
    tittle:str
    description: Optional[str] = None
    done: bool = False

tasks: List[Task] = []
next_id: int = 1

# Criar uma nova tarefa
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    global next_id
    task.id = next_id
    next_id += 1
    tasks.append(tasks)
    return task

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
@app.put("tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update_task: Task):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.tittle = update_task.tittle
    task.description = update_task.description
    task.done = update_task.done
    return task

# Exclui uma tarefa da lista
app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return

# Agora vamos fazer a execução do servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
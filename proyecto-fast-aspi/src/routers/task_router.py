from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class TaskCreate(BaseModel):
    """Lo que el cliente envía para crear una tarea. Sin id: lo asigna el servidor."""
    title: str = Field(min_length=3, max_length=100)
    description: str | None = None
    priority: str = "medium"
    tags: list[str] = Field(default_factory=list)


class TaskRead(BaseModel):
    """Lo que el servidor expone al leer una tarea. Incluye campos calculados por el servidor."""
    id: int
    title: str
    description: str | None
    priority: str
    tags: list[str]
    is_completed: bool






@task.get("/tasks", response_model=list[TaskRead])
def list_tasks() -> list[dict]:
    return TASKS




@task.post("/tasks/from-model")
def create_from_model(task: TaskCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = task.model_dump()
    new_task = {"id": len(TASKS) + 1, "is_completed": False, **data}
    TASKS.append(new_task)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validated = TaskRead.model_validate(new_task)
    return validated.model_dump()




@tasks_router.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict:
    for index, task in enumerate(TASKS):
        if task["id"] == task_id:
            deleted_task = TASKS.pop(index)

            return {
                "message": "Tarea eliminada correctamente",
                "deleted_task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )
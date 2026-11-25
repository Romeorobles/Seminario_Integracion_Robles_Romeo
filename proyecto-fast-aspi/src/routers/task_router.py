from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

TASKS: list[dict] = []


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


class TaskUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = None
    priority: str | None = None
    tags: list[str] | None = None
    is_completed: bool | None = None






@router.get("/tasks", response_model=list[TaskRead])
def list_tasks() -> list[dict]:
    return TASKS


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.post("/tasks", response_model=TaskRead, status_code=201)
def create_task(task: TaskCreate) -> dict:
    new_task = {
        "id": max((t["id"] for t in TASKS), default=0) + 1,
        "is_completed": False,
        "internal_notes": "creado desde la API",
        **task.model_dump(),
    }
    TASKS.append(new_task)
    return new_task


@router.patch("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, update: TaskUpdate) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            changes = update.model_dump(exclude_unset=True)
            # title, priority y tags no pueden quedar en null: TaskRead los exige
            changes = {k: v for k, v in changes.items() if v is not None or k == "description"}
            task.update(changes)
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.get("/tasks/{task_id}/raw-vs-validated")
def compare_raw_validated(task_id: int) -> dict:
    raw = next((t for t in TASKS if t["id"] == task_id), None)
    if raw is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    # model_validate lanza una excepción si el dict no cumple el schema de TaskRead
    validated = TaskRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validated.model_dump(),
        "validated_model_dump_json": validated.model_dump_json(),
    }




@router.post("/tasks/from-model")
def create_from_model(task: TaskCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = task.model_dump()
    new_task = {"id": max((t["id"] for t in TASKS), default=0) + 1, "is_completed": False, **data}
    TASKS.append(new_task)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validated = TaskRead.model_validate(new_task)
    return validated.model_dump()




@router.delete("/tasks/{task_id}")
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
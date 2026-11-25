# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

from routers.mp_equipo_router_ligapro import router as equipo_router
from routers.task_router import router as task_router


class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1


class MensajeCompleto(Mensaje):
    campo_interno: str


app = FastAPI(title="Curso FastAPI + uv")
app.include_router(task_router)
app.include_router(equipo_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola Romeo Robles desde FastAPI + uv",
    "autor": "Romeo Robles"}



def read_root() -> dict[str, str]:
    return {
        "mensaje": "Hola desde FastAPI + uv",
        "autor": "Ing. Francisco Higuera",
        "version": "0.1.0"
    }

@app.get("/romeo")
def endpoint_robles() -> Mensaje:
    return Mensaje(texto="Hola")

@app.get("/robles", response_model=MensajeCompleto)
def endpoint_robles():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "no debería salir"}
# mp - Router de equipos con tema LigaPro
# Autor: Romeo Robles
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/equipos", tags=["LigaPro"])


class EquipoCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=60)
    ciudad: str
    victorias: int = Field(default=0, ge=0)
    empates: int = Field(default=0, ge=0)


class EquipoUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=60)
    ciudad: str | None = None
    victorias: int | None = Field(default=None, ge=0)
    empates: int | None = Field(default=None, ge=0)


class EquipoRead(EquipoCreate):
    id: int
    puntos: int


EQUIPOS: list[dict] = [
    {"id": 1, "nombre": "Liga de Quito", "ciudad": "Quito", "victorias": 15, "empates": 10},
    {"id": 2, "nombre": "Barcelona SC", "ciudad": "Guayaquil", "victorias": 14, "empates": 10},
]


def buscar(equipo_id: int) -> dict:
    for equipo in EQUIPOS:
        if equipo["id"] == equipo_id:
            return equipo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")


def con_puntos(equipo: dict) -> EquipoRead:
    return EquipoRead(**equipo, puntos=equipo["victorias"] * 3 + equipo["empates"])


@router.get("")
def listar_equipos() -> list[EquipoRead]:
    return [con_puntos(equipo) for equipo in EQUIPOS]


@router.get("/{equipo_id}")
def obtener_equipo(equipo_id: int) -> EquipoRead:
    return con_puntos(buscar(equipo_id))


@router.post("", status_code=201)
def crear_equipo(equipo: EquipoCreate) -> EquipoRead:
    nuevo = {"id": max((e["id"] for e in EQUIPOS), default=0) + 1, **equipo.model_dump()}
    EQUIPOS.append(nuevo)
    return con_puntos(nuevo)


@router.patch("/{equipo_id}")
def actualizar_equipo(equipo_id: int, cambios: EquipoUpdate) -> EquipoRead:
    equipo = buscar(equipo_id)
    equipo.update(cambios.model_dump(exclude_unset=True, exclude_none=True))
    return con_puntos(equipo)


@router.delete("/{equipo_id}", status_code=204)
def eliminar_equipo(equipo_id: int) -> None:
    EQUIPOS.remove(buscar(equipo_id))

# Seminario de Integración

**Autor:** Romeo Robles

---

## Objetivo principal

Integrar un **backend** y un **frontend** en una misma solución. La materia empieza con un repaso de **Python**, usa **uv** para manejar los proyectos, construye APIs con **FastAPI** y las consume desde una interfaz web hecha con **Angular**, siguiendo buenas prácticas de estructura, versionamiento y despliegue.

---

## Tecnologías de la materia

### Python
Lenguaje de programación interpretado, de alto nivel y con tipado dinámico. Su sintaxis se basa en la indentación, lo que lo hace legible y fácil de aprender. Tiene **type hints** (`nombre: str`), que FastAPI aprovecha para validar datos. Se usa en backend, automatización, ciencia de datos e inteligencia artificial.

### uv
Gestor de paquetes y proyectos de Python creado por Astral y escrito en Rust. Es mucho más rápido que `pip`. En una sola herramienta reemplaza a `pip`, `venv`, `pip-tools` y `pyenv`: crea el entorno virtual, instala dependencias, fija versiones en `uv.lock` y hasta instala la versión de Python que el proyecto necesita.

```bash
uv init mi_proyecto      # crea un proyecto nuevo
uv add fastapi           # agrega una dependencia
uv run main.py           # ejecuta dentro del entorno virtual
```

### FastAPI
Framework web de Python para construir **APIs REST** rápidas y modernas. Se basa en **Starlette** (la parte web) y **Pydantic** (validación de datos con los type hints de Python). Genera documentación interactiva automática en `/docs` (Swagger UI) y soporta programación asíncrona con `async`/`await`. Se ejecuta con un servidor ASGI como **Uvicorn**.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde FastAPI"}
```

### Angular
Framework de Google para construir aplicaciones web de una sola página (**SPA**) con **TypeScript**. Organiza la interfaz en **componentes** (HTML + CSS + TypeScript). Trae de serie enrutamiento, formularios, inyección de dependencias y el cliente **HttpClient**, que se usa para consumir la API de FastAPI. Se maneja con la **Angular CLI** (`ng new`, `ng serve`, `ng generate`).

---

## ¿Cómo se integran?

```
┌──────────────┐   HTTP / JSON   ┌───────────────┐
│   Angular    │ ──────────────▶ │    FastAPI    │
│  (frontend)  │ ◀────────────── │   (backend)   │
└──────────────┘                 └───────────────┘
                                   proyecto con uv
```

Angular muestra la interfaz y hace peticiones HTTP. FastAPI recibe las peticiones, procesa los datos y responde en JSON. uv administra el entorno y las dependencias del backend en Python.

---

## Estructura del repositorio

Cada proyecto o práctica de la materia se guarda en su propia carpeta dentro de este repositorio. El archivo `.gitignore` de la raíz cubre las carpetas y subcarpetas de proyectos Python, FastAPI y Angular.

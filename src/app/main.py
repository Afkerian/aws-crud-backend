from fastapi import FastAPI

# Importa el módulo que contiene el router de imágenes
from app.api import images  
from app.db import database, engine, metadata

# Crear todas las tablas en la base de datos
metadata.create_all(engine)

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Eventos de inicio y apagado para conectar y desconectar la base de datos
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Incluir las rutas del módulo de imágenes
app.include_router(images.router, prefix="/images", tags=["images"])

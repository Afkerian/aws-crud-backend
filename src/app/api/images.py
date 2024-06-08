from fastapi import APIRouter, HTTPException, UploadFile, File
from sqlalchemy import insert, select, update, delete
from sqlalchemy.sql import func
from app.db import database, images
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import base64

router = APIRouter()

class ImageIn(BaseModel):
    title: str
    description: str

class ImageOut(BaseModel):
    id: int
    title: str
    description: str
    created_date: datetime
    image_data: Optional[str] = None  # Optional to include the image data

@router.post("/", response_model=ImageOut)
async def create_image(title: str, description: str, file: UploadFile = File(...)):
    image_data = await file.read()
    query = insert(images).values(
        title=title,
        description=description,
        image_data=image_data,
        created_date=func.now()
    )
    record_id = await database.execute(query)
    created_image = await database.fetch_one(select([images]).where(images.c.id == record_id))
    
    return {
        "id": created_image.id,
        "title": created_image.title,
        "description": created_image.description,
        "created_date": created_image.created_date,
        "image_data": base64.b64encode(created_image.image_data).decode('utf-8')
    }

@router.get("/", response_model=List[ImageOut])
async def read_images():
    query = select([images])
    result = await database.fetch_all(query)
    return [
        {
            "id": image.id,
            "title": image.title,
            "description": image.description,
            "created_date": image.created_date,
            "image_data": base64.b64encode(image.image_data).decode('utf-8')
        }
        for image in result
    ]

@router.get("/{image_id}", response_model=ImageOut)
async def read_image(image_id: int):
    query = select([images]).where(images.c.id == image_id)
    image = await database.fetch_one(query)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return {
        "id": image.id,
        "title": image.title,
        "description": image.description,
        "created_date": image.created_date,
        "image_data": base64.b64encode(image.image_data).decode('utf-8')
    }

@router.put("/{image_id}", response_model=ImageOut)
async def update_image(image_id: int, title: str, description: str, file: UploadFile = File(None)):
    update_values = {
        "title": title,
        "description": description,
    }

    if file:
        update_values["image_data"] = await file.read()
    
    query = update(images).where(images.c.id == image_id).values(**update_values)
    await database.execute(query)
    
    updated_image = await database.fetch_one(select([images]).where(images.c.id == image_id))
    
    return {
        "id": updated_image.id,
        "title": updated_image.title,
        "description": updated_image.description,
        "created_date": updated_image.created_date,
        "image_data": base64.b64encode(updated_image.image_data).decode('utf-8') if updated_image.image_data else None
    }

@router.delete("/{image_id}")
async def delete_image(image_id: int):
    query = delete(images).where(images.c.id == image_id)
    await database.execute(query)
    return {"message": "Image deleted successfully"}

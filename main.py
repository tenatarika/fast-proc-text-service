from typing import (
    Optional, List,
)

from starlette import status
from striprtf.striprtf import rtf_to_text
import uvicorn
from fastapi import (
    FastAPI,
    File,
    UploadFile,
)

import db
from proc_text import process_text, get_list_category

app = FastAPI()


@app.get("/text")
async def get_texts():
    return db.read_db()


@app.put("/text")
async def update_text(filename: str, word: str, data: dict):
    return db.update_text(filename, word, data)


@app.get("/get_by_file_name")
async def get_text_by_filename(filename: str) -> dict:
    return db.get_text_by_filename(filename)


@app.post("/file/upload")
async def upload_file(file: Optional[UploadFile] = File(...)):
    row_text = await file.read()
    text = rtf_to_text(row_text.decode('utf-8'))
    filename = file.filename
    content = {"content": text}
    db.write_db(process_text(text), filename)
    return {"content": content}


@app.delete('/file/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(filename: str) -> None:
    db.delete_file(filename)


@app.get('/category')
async def get_category():
    return db.read_category()


@app.post('/category', status_code=status.HTTP_201_CREATED)
async def upload_catgory(file: Optional[UploadFile] = File(...)):
    row_text = await file.read()
    text = rtf_to_text(row_text.decode('utf-8'))
    filename = file.filename
    content = {"content": text}
    db.write_category(filename, get_list_category(text))
    return {"content": content}


@app.put('/category')
async def update_category(filename: str, data: List[dict]):
    return db.write_category(filename, data)


@app.delete('/category', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(filename: str):
    db.delete_category(filename)


@app.get('/films')
async def suggestion(text: str):
    return db.get_saggestion_films(text)


def run() -> None:
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8888,
        loop="uvloop",
        lifespan="on",
    )


if __name__ == "__main__":
    run()

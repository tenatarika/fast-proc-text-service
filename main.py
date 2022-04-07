from typing import (
    List,
    Optional,
)
from striprtf.striprtf import rtf_to_text
import uvicorn
from fastapi import (
    FastAPI,
    File,
    UploadFile,
)

import models
import db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/text")
async def add_text(text: models.Text):
    return await db.create_text(text)


@app.get("/text", response_model=List[models.Text])
async def get_texts() -> List[models.Text]:
    return await db.get_texts()


@app.get("/text/{name}", response_model=models.Text)
async def get_text_by_name(name: str) -> models.Text:
    return await db.get_text_by_name(name)


# @app.put("/text", response_model=models.Text)
# async def update_text(model: models.Text):
#     return db.update_text(model)


@app.post("/avatar/upload")
async def upload_avatar(file: Optional[UploadFile] = File(...)):
    row_text = await file.read()
    text = rtf_to_text(row_text.decode('utf-8'))
    content = {"content": text}
    return {"content": content}


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

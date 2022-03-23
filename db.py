from typing import List

import pymongo

import models

__connection = pymongo.MongoClient("mongodb://localhost:27017")
db = __connection.db
texts_collection = db.texts


async def create_text(text: models.Text) -> None:
    texts_collection.insert_one(text.dict())
    return None


async def get_text_by_name(name: str) -> models.Text:
    return models.Text(**texts_collection.find_one({"name": name}))


async def update_text(text: models.Text) -> None:
    texts_collection.update_one(text.dict())
    return None


async def get_texts() -> models.TextsResponse:
    return models.TextsResponse(texts_collection.find({}))

from typing import List

import pymongo

import models
import json
__connection = pymongo.MongoClient("mongodb://localhost:27017")
db = __connection.db
texts_collection = db.texts


async def create_text(text: models.Text) -> None:
    texts_collection.insert_one(text.dict())
    return None


def update_text(filename: str, word: str, data_char):
    print(data_char)
    data = json.load(open("data_file.json"))
    data_file = data.get(filename)
    if not data_file:
        return "Not such file"
    for base_word in range(len(data_file["data"])):
        for item in data_file["data"][base_word]:

            if item == word:
                print(data[filename]["data"][base_word])
                data[filename]["data"][base_word][word].update(data_char)
    print(data)
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


async def get_texts() -> List[models.Text]:
    return [models.Text(**item) for item in texts_collection.find({})]


def write_db(data: dict, filename: str):
    cur_data = json.load(open("data_file.json"))
    print(cur_data)
    data_set = []
    for word, size in data.items():
        data_set.append({word: {"count": size}})
    cur_data.update({filename: {"data": data_set}})
    with open("data_file.json", "w") as write_file:
        json.dump(cur_data, write_file)


def read_db() -> dict:
    return json.load(open("data_file.json"))


def delete_file(filename: str):
    data = json.load(open("data_file.json"))
    data.pop(filename)
    print(data)
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

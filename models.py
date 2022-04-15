from pydantic import BaseModel


class Text(BaseModel):
    filename: str
    data: dict


class TextFile(BaseModel):
    url: str

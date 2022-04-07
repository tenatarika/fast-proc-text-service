from pydantic import BaseModel


class Text(BaseModel):
    name: str
    text: str


class TextFile(BaseModel):
    url: str

from pydantic import BaseModel
from pydantic.fields import List


class Text(BaseModel):
    name: str
    text: str

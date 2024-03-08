from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    title: str
    description: str | None = None

class ItemSchema(ItemBase):
    id: int
    title: str
    description: str | None = None
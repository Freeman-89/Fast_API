from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Read the next chapter of the book",

                }
            ]
        }
    }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {
                            "item": "Example schema 1!"
                        },
                        {
                            "item": "Example schema 2!"
                        }
                    ]
                }
            ]
        }
    }


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item=Form(...)):
        return cls(item=item)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'id': 1,
                    'item': "Example schema!",
                }
            ]
        }
    }

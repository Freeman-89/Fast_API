from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Read the next chapter of the book",
                    "status": "successfully"

                }
            ]
        }
    }


class Todo(BaseModel):
    id: int
    item: Item

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'id': 1,
                    'item': Item,
                }
            ]
        }
    }

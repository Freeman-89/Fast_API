from fastapi import APIRouter, Path
from model import Todo, Item

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    print('in____')
    return {'massage': 'Todo added successfully'}


@todo_router.get("/todo")
async def get_todo() -> dict:
    return {"todos": todo_list}


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: Item, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data
            return {"message": "Todo updated successfully."}

    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {'todo': todo}
    return {'massage': 'Todo with supported ID does not exist'}

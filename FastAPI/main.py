from fastapi import FastAPI, HTTPException
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field

app = FastAPI()


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    todo_name : str = Field(...,min_length=3,max_length=50, description='Name of the todo')
    todo_description : str = Field(..., description='Description of the todo')
    priority : Priority = Field(default=Priority.LOW, description='Priority of the todo')


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    todo_id : int = Field(..., description='Unique identifier of the todo')


class TodoUpdate(BaseModel):
    todo_name : Optional[str] = Field(default=None, min_length=3,max_length=50, description='Name of the todo')
    todo_description : Optional[str] = Field(default=None , description='Description of the todo')
    priority : Optional[Priority] = Field(default=None, description='Priority of the todo')


all_todos = [
    Todo(todo_id=1, todo_name="Sports", todo_description="Go to the gym", priority=Priority.MEDIUM),
    Todo(todo_id=2, todo_name="Read", todo_description="Read 10 pages", priority=Priority.LOW),
    Todo(todo_id=3, todo_name="Shop", todo_description="Go shopping", priority=Priority.HIGH),
    Todo(todo_id=4, todo_name="Study", todo_description="Study for exam", priority=Priority.HIGH),
    Todo(todo_id=5, todo_name="Meditate", todo_description="Meditate 20 minutes", priority=Priority.MEDIUM)
    ]

# GET, POST, PUT(PATCH), DELETE

# GET all todos
@app.get("/todos/")
def get_todos_all():
    return all_todos

# GET by id ---> localhost:99999/todos/2
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_id(todo_id:int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    else:
        raise HTTPException(status_code=404, detail='Todo not found ')
    
# Query paramater ----> localhost:9999/todos?first_n=3 -----> will show first n todos
@app.get("/todos", response_model=List[Todo])
def get_todos_n(todos_n : Optional[int] = None):
    
    if todos_n:
        return all_todos[:todos_n]
    else:
        return all_todos


# POST todo
@app.post("/todos",response_model=Todo)
def create_todo(todo: TodoCreate):

    new_id = max([t.todo_id for t in all_todos]) + 1

    

    new_todo = Todo(
        todo_id= new_id,
        todo_name= todo.todo_name,
        todo_description= todo.todo_description,
        priority= todo.priority
    )


    all_todos.append(new_todo)

    return new_todo


# PUT todo
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id : int, updated_todo : TodoUpdate):

    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    
    raise HTTPException(status_code=404, detail='Todo not found ')


# DELETE todo
@app.delete("/todos/{todo_id}", response_model=List[Todo])
def delete_todo(todo_id : int):

    for todo in all_todos:
        if todo.todo_id == todo_id:
            all_todos.remove(todo)
            return all_todos
        
    raise HTTPException(status_code=404, detail='Todo not found ')
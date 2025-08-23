from typing import Optional
from fastapi import FastAPI

app = FastAPI()

all_todos = [
    {'todo_id':1, 'todo_name':'Sports', 'todo_description':'Go to the gym'},
    {'todo_id':2, 'todo_name':'Read', 'todo_description':'Read 10 pages'},
    {'todo_id':3, 'todo_name':'Shop', 'todo_description':'Go shopping'},
    {'todo_id':4, 'todo_name':'Study', 'todo_description':'Study for exam'},
    {'todo_id':5, 'todo_name':'Meditate', 'todo_description':'Meditate 20 minutes'},
]


# GET, POST, PUT(PATCH), DELETE

@app.get("/")
def home():
    return {"message":"Hello World"}


# GET all todos
@app.get("/todos")
def get_todos_all():
    return all_todos


# GET by id  ---> localhost:9999/todos/2
@app.get("/todos/{todo_id}")
def get_todo_id(todo_id:int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return todo


# Query paramater ----> localhost:9999/todos?first_n=3 -----> will show first n todos
@app.get("/todos/")
def get_todos_n(todos_n : Optional[int] = None):
    if todos_n:
        return {"first_n":all_todos[:todos_n]}
    else:
        return {"all_todos":all_todos}
 

# Query paramater ----> localhost:9999/todos?todos_name="" 
@app.get("/todos/name/")
def get_todos(todo_name : Optional[str] = None):
    
    if todo_name:
        for todo in all_todos:
            if todo["todo_name"] == todo_name:
                return todo
    else:
        return all_todos




# POST todos
@app.post("/todos/")
def create_todos(todo: dict):
    
    new_id = max(t['todo_id']  for t in all_todos) + 1
    
    new_todo = {
        'todo_id' : new_id,
        'todo_name' : todo['todo_name'],
        'todo_description' : todo['todo_description'],
    }

    all_todos.append(new_todo)

    return new_todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id : int, updated_todo: dict):

    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = update_todo['todo_name']
            todo['todo_description'] = update_todo['todo_description']
            return todo
        
    return "Error, not found"

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            all_todos.remove(todo)
            return all_todos
    return "Error, not found"
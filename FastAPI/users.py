from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Start the server: fastapi dev users.py
# Stop the server: CTRL+C


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Dorian", surname="DorianDEV", url="https://dev-dorian.com/", age=29),
              User(id=2, name="Carlos", surname="CarlosDEV",
                   url="https://dev-carlos.com/", age=22),
              User(id=3, name="Maria", surname="MariaDEV", url="https://dev-maria.com/", age=30)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Dorian", "surname": "DorianDEV", "url": "https://dev-dorian.com/", "age": 29},
            {"name": "Carlos", "surname": "CarlosDEV",
                "url": "https://dev-carlos.com/", "age": 22},
            {"name": "Maria", "surname": "MariaDEV", "url": "https://dev-maria.com/", "age": 30}]


@app.get("/users")
async def users():
    return users_list

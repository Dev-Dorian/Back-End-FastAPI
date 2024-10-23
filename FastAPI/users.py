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


# http://127.0.0.1:8000/user/2  PATH
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# http://127.0.0.1:8000/userquery/?id=2  QUERY
@app.get("/userquery/")
async def userquery(id: int):
    return search_user(id)


@app.post("/user/")
async def userpost(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "User already exist"}
    else:
        users_list.append(user)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}

# Oficial Documentation: https://fastapi.tiangolo.com/es/

# Install FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# Url local: http://127.0.0.1:8000/url


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}

# Start the server: fastapi dev main.py
# Stop the server: CTRL+C

# Documentation with Swagger: http://127.0.0.1:8000/docs
# Documentation with Redocly: http://127.0.0.1:8000/redoc

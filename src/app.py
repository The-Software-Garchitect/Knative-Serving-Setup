from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helpers import do_something

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    print(item.price)
    happy = await do_something()
    return {"name": item.name,
            "happy": happy}

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

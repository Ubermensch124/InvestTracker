""" Basic fastapi application """

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Main root, just return json"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    """Second root, return json too"""
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

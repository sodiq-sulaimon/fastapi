
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Annotated

# Simple API
app = FastAPI()

@app.get("/")
def root():
    return "Hey there! Welcome to my API"


# Path parameters with types
@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"Item Id: ": item_id}

# Path parameters containing paths
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"File path": file_path}

# Request Body
#from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None 
    price: float 
    tax: float | None = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"Price with tax": price_with_tax})
        return {item.name: item_dict["Price with tax"]}
    return {item.name: item.price}

# Query parameters
dummy_items = [{1 : "Mango"}, {2 : "Banana"}, {3 : "Orange"}, {4 : "Apple"}]

@app.get("/items_query")
def read_item(skip: int, limit: int = 10, sort: bool | None = None): # not giving default values to query parameters makes it required, sort is added to show optional query parameter.
    return dummy_items[skip: skip + limit]

# Request body + path parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

# Query parameters and string validation
# from fastapi import Query
# from typing import Annotated

dummy_items = [{1 : "Mango"}, {2 : "Banana"}, {3 : "Orange"}, {4 : "Apple"}]

@app.get("/items_valquery")
async def read_item(skip: int = 0, limit: Annotated[int | None, Query(le=50)] = None): # Used to set the max number for option query parameter 'limit'
    if limit:
        return dummy_items[skip:skip + limit]
    return dummy_items[skip:2]

# Path parameters and numeric validations
# from FastAPI import Path

@app.get("/items_path/{item_id}")
async def read_item(item_id: Annotated[int, Path(title = "Id of the item")],
                    q: Annotated[str | None, Query(alias = 'item-query')]):
    results = {"Item_id": item_id}
    if q:
        results.update({"q": q})
    return results



from fastapi import FastAPI
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

post_app = FastAPI()

class Post(BaseModel):
    user_id : int
    title: str
    content: str
    draft: bool = False
    rating: Optional[int] = None

@post_app.get("/")
def root():
    return {"Message: Hello, World!"}

@post_app.post("/createpost")
# def create_post(new_post: dict = Body(...)):
def create_post(new_post: Post):
    print(new_post.user_id, ":", new_post.title)
    print("Rating: ", new_post.rating)
    if new_post.draft is True:
        return ("Post saved as draft.")
    else:
        new_post.dict
        return {"Data": new_post}


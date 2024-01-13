from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

post_app = FastAPI()

class Post(BaseModel):
    user_id : int
    title: str
    content: str
    draft: bool = False

@post_app.get("/")
def root():
    return {"Message: Hello, World!"}

@post_app.post("/createpost")
# def create_post(new_post: dict = Body(...)):
def create_post(new_post: Post):
    if new_post.draft is True:
        return ("Post saved as draft.")
    else:
        return new_post.content


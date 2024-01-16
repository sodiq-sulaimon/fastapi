from fastapi import FastAPI
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    draft: bool = False
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"Message: Hello, World!"}

saved_posts = []

@app.post("/posts")
# def create_post(new_post: dict = Body(...)):
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 1000000)
    saved_posts.append(post_dict)
    if post.draft is True:
        return ("Post saved as draft.")
    else:
        return post.content


@app.get("/posts")
def get_posts():
    return saved_posts

# sample id
id = randrange(1, 1000000)
@app.get("/posts/{id}")
def get_one_post():
    return {"Details": f"Here is post {id}"}

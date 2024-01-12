from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def home():
    return "Hi there! Welcome to my API!"

@app.get("/models")
def model():
    return """Welcome to the Model page.
    Here is where to find the different models."""

@app.post("/requests")
def request(body: dict = Body(...)):
    print(body)
    return "Request successfully received."

@app.post("/test")
def test(test_body: dict = Body(...)):
    return test_body["1"], test_body["4"]

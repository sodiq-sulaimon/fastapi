from pydantic import BaseModel
from datetime import datetime
from typing import Union

class User(BaseModel):
    id: int
    name: str = "John Smith"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []

test_data = {
"id": "123",
"signup_ts": "2017-06-01 12:22",
"friends": [1, "2", b"3"], #pydantic automatically converts each element into str
}

user = User(**test_data) # ** unpacks the dictionary
print(user.friends) 

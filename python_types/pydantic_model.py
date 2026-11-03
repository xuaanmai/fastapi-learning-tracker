'''
Pydantic dùng để convert giá trị về đúng data type nó được gán
'''

from pydantic import BaseModel

from datetime import datetime


class User(BaseModel):
    id: int
    name: str = "Jane Doe"
    signup_ts: datetime | None=None
    friends: list[int] = []

data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**data)
print(user)
print(user.id)
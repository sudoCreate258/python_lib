from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int

try:
    User(id="abc")
except ValidationError as e:
    print(e)

from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl

class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl
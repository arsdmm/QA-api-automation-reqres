from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List

class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

class SingleUserResponse(BaseModel):
    data: User

class ListUsersResponse(BaseModel):
    page: int
    data: List[User]

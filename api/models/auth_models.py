from pydantic import BaseModel


class LoginSuccessResponse(BaseModel):
    token: str

class ErrorResponse(BaseModel):
    error: str
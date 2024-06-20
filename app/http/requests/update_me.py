from pydantic import BaseModel


class UpdateMe(BaseModel):
    email: str
    password: str

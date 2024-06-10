from pydantic import BaseModel


class AdminSignIn(BaseModel):
    email: str
    password: str

from pydantic import BaseModel

from ...models.admin_user import AdminUser as Model


class AdminUser(BaseModel):
    id: str
    name: str
    email: str

    @classmethod
    def from_model(cls, model: Model) -> 'AdminUser':
        return cls(**model.dict())

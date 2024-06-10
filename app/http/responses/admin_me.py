from pydantic import BaseModel

from app.models.admin_user import AdminUser


class AdminMe(BaseModel):
    id: str
    name: str
    email: str

    @classmethod
    def from_model(cls, model: AdminUser) -> 'AdminMe':
        return cls(id=str(model.id), name=model.name, email=model.email)

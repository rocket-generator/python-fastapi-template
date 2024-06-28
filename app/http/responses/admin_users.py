from pydantic import BaseModel

from .admin_user import AdminUser
from ...models.admin_user import AdminUser as Model


class AdminUsers(BaseModel):
    data: [AdminUser]
    count: str

    @classmethod
    def from_model(cls, data: [Model], count: int) -> 'AdminUsers':
        data = [AdminUser.from_model(model) for model in data]
        return cls(data=data, count=count)

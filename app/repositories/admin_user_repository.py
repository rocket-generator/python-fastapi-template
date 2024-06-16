from typing import Type, cast

from ..models.admin_user import AdminUser
from .base_repository import BaseRepository


class AdminUserRepository(BaseRepository):
    model = AdminUser

    def get_by_email(self, email: str) -> AdminUser | None:
        return self._db.query(self.model).filter(
            cast("ColumnElement[bool]", AdminUser.email == email)).first()

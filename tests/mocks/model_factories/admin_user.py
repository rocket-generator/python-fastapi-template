from typing import Optional

from sqlalchemy_model_faker import factory

from app.models.admin_user import AdminUser


def admin_user_factory(_id: Optional[str] = None,
                       data: Optional[dict] = None) -> AdminUser:
    fields = {}
    if _id is not None:
        fields["id"] = _id
    if data is not None:
        for key, value in data.items():
            fields[key] = value
    return factory(AdminUser).make(fields)

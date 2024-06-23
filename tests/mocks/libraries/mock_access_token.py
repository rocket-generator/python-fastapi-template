from datetime import datetime, timedelta, timezone
from typing import Optional

from faker import Faker

from app.interfaces.libraries.access_token_interface import \
    AccessTokenInterface


class MockAccessToken(AccessTokenInterface):

    @staticmethod
    def create_access_token(data: dict,
                            expires_delta: timedelta | None = None):
        faker_instance = Faker()
        _id = faker_instance.uuid4()
        return faker_instance.jwt.encode({
            "user_id":
            _id,
            "sub":
            _id,
            "exp":
            datetime.now(timezone.utc) + expires_delta
        })

    @staticmethod
    def extract_from_token(token: str) -> Optional[dict]:
        faker_instance = Faker()
        _id = faker_instance.uuid4()
        return {"user_id": _id, "sub": _id}

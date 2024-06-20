from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, exceptions


from app.config import config
from app.exceptions.client_side_error import ClientSideError


class JWT(object):

    @staticmethod
    def create_access_token(data: dict,
                            expires_delta: timedelta | None = None):
        claims = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(
                timezone.utc) + timedelta(minutes=config.JWT_EXPIRE_MINUTES)
        claims.update({"exp": expire})
        encoded_jwt = jwt.encode(claims,
                                 config.JWT_SECRET,
                                 algorithm=config.JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def extract_from_jwt(token: str) -> Optional[dict]:
        try:
            return jwt.decode(token,
                              config.JWT_SECRET,
                              algorithms=[config.JWT_ALGORITHM])
        except exceptions.ExpiredSignatureError as e:
            return None
        except exceptions.JWTError as e:
            raise ClientSideError(f"JWT Error: {e}")

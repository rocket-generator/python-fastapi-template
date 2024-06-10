from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.config import config
from app.exceptions.client_side_exception import ClientSideException


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
    def extract_from_jwt(token: str) -> dict:
        try:
            return jwt.decode(token,
                              config.JWT_SECRET,
                              algorithms=[config.JWT_ALGORITHM])
        except JWTError as e:
            raise ClientSideException(f"JWT Error: {e}")

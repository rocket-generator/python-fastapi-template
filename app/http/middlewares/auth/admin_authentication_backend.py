from injector import inject
from sqlalchemy.orm import scoped_session
from starlette.authentication import (AuthCredentials, AuthenticationBackend,
                                      AuthenticationError, SimpleUser)

from ....config import Config
from ....libraries.jwt import JWT
from ....services.admin_user_service import AdminUserService


class AdminAuthenticationBackend(AuthenticationBackend):

    @inject
    def __init__(self, _admin_user_service: AdminUserService, _jwt: JWT,
                 _db: scoped_session, _config: Config):
        self._admin_user_service = _admin_user_service
        self._jwt = _jwt
        self._db = _db
        self._config = _config

    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, token = auth.split()
            if scheme.lower() != 'bearer':
                return
            user = self._admin_user_service.get_admin_user_by_token(token)

        except (ValueError, UnicodeDecodeError) as exc:
            raise AuthenticationError('Invalid auth token')
        except Exception as exc:
            raise AuthenticationError('Invalid auth token')

        if user is None:
            raise AuthenticationError('Invalid auth token')

        return AuthCredentials(["admin_authenticated"]), user

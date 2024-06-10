from typing import Optional, Tuple

from injector import Injector, inject

from ..config import Config
from ..libraries import Hash, JWT
from ..models.admin_user import AdminUser
from ..repositories.admin_user_repository import AdminUserRepository


class AdminUserService(object):

    @inject
    def __init__(self, admin_user_repository: AdminUserRepository, _hash: Hash,
                 _jwt: JWT, _config: Config):
        self._admin_user_repository = admin_user_repository
        self._hash = _hash
        self._jwt = _jwt
        self._config = _config

    def sign_in(self, email: str,
                password: str) -> Optional[Tuple[AdminUser, str]]:
        admin_user = self._admin_user_repository.get_by_email(email)

        if admin_user is None:
            return None

        if self._hash.verify_hash(password, admin_user.password):
            return admin_user, self.generate_access_token(str(admin_user.id))

        return None

    def generate_access_token(self, user_id: str) -> str:
        encoded_jwt = self._jwt.create_access_token({
            "sub": user_id,
            "user_id": user_id
        })
        return encoded_jwt

    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        decoded_jwt = self._jwt.extract_from_jwt(access_token)
        admin_user_id = decoded_jwt["user_id"]
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)

        return admin_user

from typing import Optional, Tuple

from injector import Injector, inject
from sqlalchemy.orm import scoped_session

from ..config import Config
from ..exceptions import ClientSideError
from ..interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from ..libraries import JWT, Hash
from ..models.admin_user import AdminUser
from ..repositories.admin_user_repository import AdminUserRepository


class AdminUserService(AdminUserServiceInterface):

    @inject
    def __init__(self, admin_user_repository: AdminUserRepository, _hash: Hash,
                 _jwt: JWT, _db: scoped_session, _config: Config):
        self._admin_user_repository = admin_user_repository
        self._hash = _hash
        self._jwt = _jwt
        self._db = _db
        self._config = _config

    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:
        admin_user = self._admin_user_repository.get_by_email(email)
        if admin_user is None:
            return None, None

        if self._hash.verify_hash(password, admin_user.password):
            return admin_user, self.generate_access_token(str(admin_user.id))

        return None, None

    def generate_access_token(self, user_id: str) -> str:
        encoded_jwt = self._jwt.create_access_token({
            "sub": user_id,
            "user_id": user_id
        })
        return encoded_jwt

    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        decoded_jwt = self._jwt.extract_from_jwt(access_token)
        if decoded_jwt is None:
            return None
        admin_user_id = decoded_jwt["user_id"]
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)

        return admin_user

    def get_admin_user_by_id(self, id: str) -> Optional[AdminUser]:
        admin_user = self._admin_user_repository.get_by_id(id)
        return admin_user

    def update_admin_user(self, admin_user_id: str,
                          admin: dict) -> Optional[AdminUser]:
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)
        if admin_user is None:
            raise ClientSideError("Admin user not found")

        if "password" in admin:
            admin["password"] = self._hash.generate_hash(admin["password"])

        updated_admin_user = self._admin_user_repository.update(
            admin_user_id, admin)
        return updated_admin_user

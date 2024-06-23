from typing import Optional, Tuple

from injector import Injector, inject

from ..config import Config
from ..exceptions import ClientSideError
from ..interfaces.libraries.access_token_interface import AccessTokenInterface
from ..interfaces.libraries.hash_interface import HashInterface
from ..interfaces.repositories.admin_user_repository_interface import \
    AdminUserRepositoryInterface
from ..interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from ..models.admin_user import AdminUser


class AdminUserService(AdminUserServiceInterface):

    @inject
    def __init__(self, admin_user_repository: AdminUserRepositoryInterface,
                 _hash: HashInterface, _access_token: AccessTokenInterface,
                 _config: Config):
        self._admin_user_repository = admin_user_repository
        self._hash = _hash
        self._access_token = _access_token
        self._config = _config

    def sign_in(self, email: str,
                password: str) -> Tuple[Optional[AdminUser], Optional[str]]:
        admin_user = self._admin_user_repository.get_by_email(email)
        if admin_user is None:
            return None, None

        if self._hash.verify_hash(password, admin_user.password):
            return admin_user, self.generate_access_token(str(admin_user.id))

        return None, None

    def generate_access_token(self, admin_user_id: str) -> str:
        encoded_jwt = self._access_token.create_access_token({
            "sub":
            admin_user_id,
            "user_id":
            admin_user_id
        })
        return encoded_jwt

    def get_admin_user_by_token(self,
                                access_token: str) -> Optional[AdminUser]:
        decoded_jwt = self._access_token.extract_from_token(access_token)
        if decoded_jwt is None:
            return None
        admin_user_id = decoded_jwt["user_id"]
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)

        return admin_user

    def get_admin_user_by_id(self, admin_user_id: str) -> Optional[AdminUser]:
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)
        return admin_user

    def update_admin_user(self, admin_user_id: str,
                          data: dict) -> Optional[AdminUser]:
        admin_user = self._admin_user_repository.get_by_id(admin_user_id)
        if admin_user is None:
            raise ClientSideError("Admin user not found")

        if "password" in data:
            data["password"] = self._hash.generate_hash(data["password"])

        updated_admin_user = self._admin_user_repository.update(
            admin_user_id, data)
        return updated_admin_user

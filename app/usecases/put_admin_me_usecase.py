from typing import Optional, Tuple

from ..interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from ..interfaces.usecases.put_admin_me_usecase_interface import \
    PutAdminMeUsecaseInterface
from ..models.admin_user import AdminUser


class PutAdminMeUsecase(PutAdminMeUsecaseInterface):

    def __init__(self, admin_user_service: AdminUserServiceInterface):
        self.admin_user_service = admin_user_service

    def handle(self, admin_user_id: str, data: dict) -> Optional[AdminUser]:
        return self.admin_user_service.update_admin_user(admin_user_id, data)

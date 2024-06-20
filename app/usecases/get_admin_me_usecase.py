from typing import Optional, Tuple

from ..interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from ..interfaces.usecases.get_admin_me_usecase_interface import \
    GetAdminMeUsecaseInterface
from ..models.admin_user import AdminUser


class GetAdminMeUsecase(GetAdminMeUsecaseInterface):

    def __init__(self, admin_user_service: AdminUserServiceInterface):
        self.admin_user_service = admin_user_service

    def handle(self, admin_user_id: str) -> Optional[AdminUser]:
        return self.admin_user_service.get_admin_user_by_id(admin_user_id)

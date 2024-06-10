from injector import Injector, inject
from .base_seeder import BaseSeeder
from app.models.admin_user import AdminUser


class AdminUserSeeder(BaseSeeder):
    model = AdminUser

    def get_data(self) -> list:
        return [
            {'name': 'Test User', 'email': 'test@example.com', 'password': self._hash.generate_hash("test")},
        ]

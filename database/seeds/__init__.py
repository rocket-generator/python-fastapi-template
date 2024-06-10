from app.bootstrap.container import build_container
from .admin_user_seeder import AdminUserSeeder


def seed():
    _injector = build_container()
    AdminUserSeeder(_injector).run()

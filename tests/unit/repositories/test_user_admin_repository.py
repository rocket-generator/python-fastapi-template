from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from app.repositories.admin_user_repository import AdminUserRepository


def test_create_instance():

    repository = AdminUserRepository(db=UnifiedAlchemyMagicMock())

    assert repository is not None

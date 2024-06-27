from app.services.admin_user_service import AdminUserService
from tests.mocks.libraries.mock_access_token import MockAccessToken
from tests.mocks.libraries.mock_hash import MockHash
from tests.mocks.repositories.mock_admin_user_repository import \
    MockAdminUserRepository
from app.config import config


def test_create_instance():

    service = AdminUserService(admin_user_repository=MockAdminUserRepository(),
                               _hash=MockHash(),
                               _access_token=MockAccessToken(),
                               _config=config)

    assert service is not None

from app.usecases.get_admin_me_usecase import GetAdminMeUsecase
from tests.mocks.services.mock_admin_user_service import MockAdminUserService


def test_handle_get_admin_me_usecase():
    usecase = GetAdminMeUsecase(MockAdminUserService())
    admin_user = usecase.handle("acc57e72-860a-5efa-a5fe-f7bbf745c71f")
    assert admin_user is not None
    assert admin_user.id == "acc57e72-860a-5efa-a5fe-f7bbf745c71f"

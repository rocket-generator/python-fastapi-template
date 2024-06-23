import faker

from app.usecases.put_admin_me_usecase import PutAdminMeUsecase
from tests.mocks.services.mock_admin_user_service import MockAdminUserService


def test_handle_put_admin_me_usecase():
    _faker = faker.Faker()
    new_email = _faker.email()
    usecase = PutAdminMeUsecase(MockAdminUserService())
    admin_user = usecase.handle("acc57e72-860a-5efa-a5fe-f7bbf745c71f", {
        "email": new_email,
    })
    assert admin_user is not None

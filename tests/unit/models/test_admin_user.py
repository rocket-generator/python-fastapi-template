from faker import Faker

from app.models.admin_user import AdminUser


def test_create_model_instance():
    faker_instance = Faker()

    model = AdminUser(email=faker_instance.email(),
                      password=faker_instance.password())
    assert model is not None

import bcrypt
from faker import Faker

from app.interfaces.libraries.hash_interface import HashInterface
from app.libraries import Hash


class MockHash(HashInterface):

    @staticmethod
    def generate_hash(key: str) -> str:
        faker_instance = Faker()
        return faker_instance.password()

    @staticmethod
    def verify_hash(key: str, _hash: str) -> bool:
        return True

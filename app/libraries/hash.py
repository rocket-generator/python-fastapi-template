from passlib.context import CryptContext


class Hash(object):

    @staticmethod
    def generate_hash(key: str) -> str:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(key)

    @staticmethod
    def verify_hash(key: str, _hash: str) -> bool:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(key, _hash)

from logging import Logger

import bcrypt

from app.interfaces.libraries.hash_interface import HashInterface


class Hash(HashInterface):

    def __init__(self, logger: Logger):
        self._logger = logger

    @staticmethod
    def generate_hash(key: str) -> str:
        _byte_key = key.encode('utf-8')
        salt = bcrypt.gensalt()
        _hash = bcrypt.hashpw(_byte_key, salt)
        return _hash.decode('utf-8')

    @staticmethod
    def verify_hash(key: str, _hash: str) -> bool:
        _byte_key = key.encode('utf-8')
        _byte_hash = _hash.encode('utf-8')
        return bcrypt.checkpw(_byte_key, _byte_hash)

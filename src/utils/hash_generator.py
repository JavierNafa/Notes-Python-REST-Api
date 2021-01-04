from os import urandom
from hashlib import pbkdf2_hmac
from src.utils.response_error import ResponseError


def hash_password(password: str):
    salt = urandom(32)
    password_encoded = password.encode('utf-8')
    key = pbkdf2_hmac('sha256', password_encoded, salt, 1000, dklen=128)
    storage = salt + key
    return storage


def decode_hash(password: str, hash_storage: bytes):
    salt = hash_storage[:32]
    key_storage = hash_storage[32:]
    password_encoded = password.encode('utf-8')
    key = pbkdf2_hmac('sha256', password_encoded, salt, 1000, dklen=128)
    if key.hex() == key_storage.hex():
        return True
    return False

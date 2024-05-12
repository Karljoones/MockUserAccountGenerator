import hashlib
import uuid

class User:
    _uuid = None
    name = None
    email = None
    _password = None
    locale = None
    language = None
    country = None
    signup_time = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person({self.name}, {self.email}, {self._password})'
    
    def set_uuid(self):
        self._uuid = uuid.uuid4()

    def get_uuid(self):
        return self._uuid
    
    def set_password(self, password):
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        self._password = hash_object.hexdigest()
    
    def get_password(self):
        return self._password
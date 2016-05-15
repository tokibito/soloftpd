import hashlib
from pyftpdlib.authorizers import AuthenticationFailed


class Authorizer:
    def __init__(self, username, password, permission=None):
        self.username = username
        self.password = password
        self.permission = permission or "elradfmw"

    def has_user(self, username):
        return self.username == username

    def validate_password(self, password):
        return self.password == hashlib.sha1(password).hexdigest()

    def validate_authentication(self, username, password, handler):
        if self.username == username and self.validate_password(password):
            return
        raise AuthenticationFailed("Authentication failed.")

    def has_perm(self, username, perm, path=None):
        return perm in self.permission

    def get_perms(self, username):
        return self.permission

    def get_msg_login(self, username):
        return "Login successful."

    def get_msg_quit(self, username):
        return "Goodbye."

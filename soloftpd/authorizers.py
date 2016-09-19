import sys
import hashlib
from pyftpdlib.authorizers import AuthenticationFailed


class Authorizer:
    def __init__(self, username, password, directory, permission=None):
        self.username = username
        self.password = password
        self.directory = directory
        self.permission = permission or "elradfmw"

    def has_user(self, username):
        return self.username == username

    def validate_password(self, password):
        return self.password == make_password_hash(password)

    def validate_authentication(self, username, password, handler):
        if self.username == username and self.validate_password(password):
            return
        raise AuthenticationFailed("Authentication failed.")

    def get_home_dir(self, username):
        return self.directory

    def has_perm(self, username, perm, path=None):
        return perm in self.permission

    def get_perms(self, username):
        return self.permission

    def get_msg_login(self, username):
        return "Login successful."

    def get_msg_quit(self, username):
        return "Goodbye."

    def impersonate_user(self, username, password):
        pass

    def terminate_impersonation(self, username):
        pass


def make_password_hash(password):
    return hashlib.sha1(password.encode('utf8')).hexdigest()


def main():
    if len(sys.argv) < 2:
        sys.exit()
    print("password hash:")
    print(make_password_hash(sys.argv[1]))


if __name__ == '__main__':
    main()

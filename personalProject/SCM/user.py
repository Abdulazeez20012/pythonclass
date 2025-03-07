import re
import bcrypt


class User:
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    PASSWORD_PATTERN = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    def __init__(self, email, password):
        if not re.match(User.EMAIL_PATTERN, email):
            raise ValueError("Invalid email format")
        if not re.match(User.PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must be at least 8 characters, contain a number, an uppercase letter, and a special character")

        self.email = email
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

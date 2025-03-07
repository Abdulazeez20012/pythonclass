from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, email: str, password: str, name: str):
        if not email:
            raise ValueError("Email cannot be empty.")
        self.email = email
        self.password = password
        self.name = name

    def login(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password

    @abstractmethod
    def view_courses(self):
        pass

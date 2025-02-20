from Dsa_Function.entries import Entries

class Diary:
    def __init__(self, diary_id):
        self.diary_id = diary_id
        self.entries = Entries()
        self.is_locked = True
        self.is_logged_in = False

    def login(self, password):
        if password == "secret":  # Example password
            self.is_logged_in = True
        else:
            raise ValueError("Incorrect password")

    def logout(self):
        self.is_logged_in = False

    def lock_diary(self):
        self.is_locked = True

    def unlock_diary(self):
        self.is_locked = False

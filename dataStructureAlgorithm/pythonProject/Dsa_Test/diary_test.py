import unittest
from Dsa_Function.diary import Diary

class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary(1)

    def test_login(self):
        self.diary.login("secret")
        self.assertTrue(self.diary.is_logged_in)

    def test_login_incorrect_password(self):
        with self.assertRaises(ValueError):
            self.diary.login("wrong_password")

    def test_lock_unlock_diary(self):
        self.diary.unlock_diary()
        self.assertFalse(self.diary.is_locked)
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked)

    def test_create_entry(self):
        self.diary.login("secret")
        self.diary.unlock_diary()
        self.diary.entries.create_entry(1, "Title", "Content")
        self.assertIn(1, self.diary.entries.entries)

    def test_update_entry(self):
        self.diary.login("secret")
        self.diary.unlock_diary()
        self.diary.entries.create_entry(1, "Title", "Content")
        self.diary.entries.update_entry(1, "New Title", "New Content")
        self.assertEqual(self.diary.entries.entries[1].title, "New Title")

    def test_delete_entry(self):
        self.diary.login("secret")
        self.diary.unlock_diary()
        self.diary.entries.create_entry(1, "Title", "Content")
        self.diary.entries.delete_entry(1)
        self.assertNotIn(1, self.diary.entries.entries)

    def test_view_entry(self):
        self.diary.login("secret")
        self.diary.unlock_diary()
        self.diary.entries.create
        self.assertEqual()
import unittest
from Dsa.my_encrypt import my_encrypt


class encrypt_test(unittest.TestCase):
    def test_That_Class_Exist(self):
        pass

    def test_for_input(self):
        actual = my_encrypt.encrypt_text("Hello, World")
        expected = "Uryyb, Jbeyq"
        self.assertEqual(actual, expected)
    def test_for_input_2(self):
        actual = my_encrypt.encrypt_text("Welcome , Bro")
        expected = "Jrypbzr , Oeb"
        self.assertEqual(actual, expected)

    def test_if_encrypt_Can_Accept_Strings(self):
        actual = my_encrypt.encrypt_text("Hello, World")
        expected = "Uryyb, Jbeyq"
        self.assertEqual(actual, expected)
        self.assertTrue(actual, "Uryyb, Jbeyq")



if __name__ == '__main__':
    unittest.main()

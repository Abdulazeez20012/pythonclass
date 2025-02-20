import unittest
from Dsa_Function.azBank.account import Account

class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account("1234567890", "Azeez", "Az", "1234", 100)

    def test_that_can_deposit_to_account(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_that_can_withdraw_from_account(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_that_when_we_withdraw_amount_greater_than_balance_raise_value_error(self):
        self.account.deposit(150)
        self.assertEqual(self.account.get_balance(), 250)
        with self.assertRaises( ValueError):
            self.account.withdraw(300)

    def test_that_account_should_raise_value_error_when_negative_deposit_is_entered(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_that_account_should_raise_value_error_when_an_invalid_pin_is_entered_eg_pin_lower_or_higher_that_4(self):
        with self.assertRaises(ValueError):
            Account("0987654321", "Azeez", "Az" "123", 50)
        with self.assertRaises(ValueError):
            Account("0987654322", "bola", "Az", "12345", 50)



if __name__ == '__main__':
    unittest.main()
import unittest
from Dsa_Function.azBank.bank import Bank

class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account1 = self.bank.create_account("Azeez", "muhammad", "4321", 200)
        self.account2 = self.bank.create_account("muhammad", "azeez", "9876", 300)

    def test_create_account(self):
        self.assertIsNotNone(self.account1.account_number)
        self.assertEqual(self.bank.check_balance(self.account1.account_number), 200)

    def test_that_can_deposit_100_and_balance_from_200_to_300(self):
        self.bank.deposit(self.account1.account_number, 100)
        self.assertEqual(self.bank.check_balance(self.account1.account_number), 300)

    def test_that_withdraw_50_from_my_initial_deposit_and_balance_update_to_150(self):
        self.bank.withdraw(self.account1.account_number, 50)
        self.assertEqual(self.bank.check_balance(self.account1.account_number), 150)

    def test_that_can_transfer_50_from_account1_to_account2(self):
        self.bank.transfer(self.account1.account_number, self.account2.account_number, 50)
        self.assertEqual(self.bank.check_balance(self.account1.account_number), 150)
        self.assertEqual(self.bank.check_balance(self.account2.account_number), 350)

    def test_that_can_close_account(self):
        self.bank.close_account(self.account1.account_number)
        with self.assertRaises(ValueError):
            self.bank.check_balance(self.account1.account_number)

if __name__ == '__main__':
    unittest.main()
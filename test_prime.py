import unittest
import is_prime
class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        
        self.assertTrue(is_prime(2))  
        self.assertTrue(is_prime(3))  
        self.assertTrue(is_prime(5))  
        self.assertTrue(is_prime(7))  
        
       
       self.assertFalse(is_prime(1))  
       self.assertFalse(is_prime(4))  
       self.assertFalse(is_prime(6))  
       self.assertFalse(is_prime(9)) 
       self.assertFalse(is_prime(10)) 










if __name__ == '__main__':
    unittest.main()

from demo.example import is_prime

import unittest

class PrimeTests(unittest.TestCase):
    def test_simple_prime(self):
        self.assertTrue(is_prime(2))
    
    def test_less_than_two(self):
        self.assertFalse(is_prime(1))

    def test_even_number(self):
        self.assertFalse(is_prime(98))
    
    def test_negative_value(self):
        self.assertFalse(is_prime(-19))
    
    def test_small_square_value(self):
        self.assertFalse(is_prime(9))
    
    def test_larger_prime(self):
        self.assertTrue(is_prime(7919))
    
    def test_square_value(self):
        self.assertFalse(is_prime(81))
    
    def test_known_prime(self):
        self.assertTrue(is_prime(17))
    
    def test_list_of_values(self):
        input = [2, 3, 7, 13, 20]
        expected = [True, True, True, True, False]
        result = is_prime(input)
        self.assertListEqual(result, expected)
    
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            is_prime("invalid")
    
    def test_invalid_types_in_list(self):
        input = [17, 'invalid', True, 19]
        expected = [True, True]
        result = is_prime(input)
        self.assertListEqual(result, expected)
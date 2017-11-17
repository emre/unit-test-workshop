import unittest

# https://docs.python.org/3/library/unittest.html

from is_prime import is_prime


class TestIsPrime(unittest.TestCase):

    def test_success_case(self):
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(11), True)

    def test_failure_case(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(900000), False)

    def test_special_logic(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_prime("caner")

    def test_big_number(self):
        with self.assertRaises(MemoryError):
            is_prime(10000000000000000)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_prime(-10)

if __name__ == '__main__':
    unittest.main()
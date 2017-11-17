# -*- coding: utf-8 -*-

import unittest

from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_success(self):
        self.assertEqual(is_palindrome("kacak"), True)

    def test_failure(self):
        self.assertEqual(is_palindrome("caner"), False)

    def test_sentence(self):
        self.assertEqual(
            is_palindrome("At, sahibi gibi hasta."), True)

    def test_integers(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)

    def test_integers_as_string(self):
        self.assertEqual(is_palindrome("123123"), True)

    def test_upper_i(self):
        self.assertEqual(is_palindrome("İKİ"), True)
        self.assertEqual(is_palindrome("IKI"), True)


unittest.main()
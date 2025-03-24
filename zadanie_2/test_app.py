import unittest
from app import is_valid_email, calculate_area, sort_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("user@com"))
    
    def test_calculate_area(self):
        self.assertEqual(calculate_area("circle", (3,)), 28.27431)
        self.assertEqual(calculate_area("rectangle", (4, 5)), 20)
        self.assertEqual(calculate_area("triangle", (3, 6)), 9)
    
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort_numbers([-5, 10, 0]), [-5, 0, 10])
    
    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("24-03-2025"), "2025-03-24")
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
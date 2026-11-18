#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer."""

    def test_ordered_list(self):
        """The max of an ordered list is its last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max is found in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max is found at the beginning of the list."""
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_max_at_end(self):
        """The max is found at the end of the list."""
        self.assertEqual(max_integer([3, 1, 2, 10]), 10)

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling the function without argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The max of negative numbers is the closest to zero."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """The max works with positive and negative numbers."""
        self.assertEqual(max_integer([-5, 0, 5, -10]), 5)

    def test_duplicates(self):
        """A repeated max value is returned once."""
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_floats(self):
        """The max works with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """The max works with integers and floats together."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """The max works with big integers."""
        self.assertEqual(max_integer([10 ** 20, 1, 10 ** 19]), 10 ** 20)

    def test_tuple(self):
        """The function also accepts a tuple."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string(self):
        """The function returns the biggest character of a string."""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """The function compares strings alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types(self):
        """Comparing a string with an integer raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none_argument(self):
        """None has no length so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """An integer has no length so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_list_not_changed(self):
        """The function does not change the list."""
        numbers = [3, 1, 2]
        max_integer(numbers)
        self.assertEqual(numbers, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()

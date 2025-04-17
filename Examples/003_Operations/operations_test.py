import operations
import unittest

class TestOperations(unittest.TestCase):

    def test_add(self):
        # test positive numbers
        self.assertEqual(operations.add(10, 5), 15)
        # test positive number and negative number
        self.assertEqual(operations.add(-1, 1), 0)
        # test negative numbers
        self.assertEqual(operations.add(-1, -1), -2)

    def test_subtract(self):
        # test positive numbers
        self.assertEqual(operations.subtract(10, 5), 5)
        # test positive number and negative number
        self.assertEqual(operations.subtract(-1, 1), -2)
        # test negative numbers
        self.assertEqual(operations.subtract(-1, -1), 0)

    def test_multiply(self):
        # test positive numbers
        self.assertEqual(operations.multiply(10, 5), 50)
        # test positive number and negative number
        self.assertEqual(operations.multiply(-1, 1), -1)
        # test negative numbers
        self.assertEqual(operations.multiply(-1, -1), 1)

    # def test_divide(self):
    def test_divide(self):
        # test positive numbers
        self.assertEqual(operations.divide(10, 5), 2)
        # test positive number and negative number
        self.assertEqual(operations.divide(-1, 1), -1)
        # test negative numbers
        self.assertEqual(operations.divide(-1, -1), 1)
        # test decimal result
        self.assertEqual(operations.divide(5, 2), 2.5)

        # test ValueError
        self.assertRaises(ValueError, operations.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
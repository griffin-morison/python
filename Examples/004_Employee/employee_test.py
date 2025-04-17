import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    
    def setUp(self):
        print('setUp')
        # create Employee objects
        self. emp_1 = Employee('Bob', 'Smith', 50000)
        self.emp_2 = Employee('Amy', 'Williams', 75000)

    def tearDown(self):
        print('tearDown\n')
        pass

    # test Employee email method
    def test_email(self):
        print('test_email')
        # test Employee email method
        self.assertEqual(self.emp_1.email, 'Bob.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Amy.Williams@email.com')

        # change Employee objects names
        self.emp_1.first = 'John'
        self.emp_2.last = 'Smith'

        # test Employee email method again
        self.assertEqual(self.emp_1.email, 'John.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Amy.Smith@email.com')

    # test Employee fullname method
    def test_fullname(self):
        print('test_fullname')
        # test Employee fullname method
        self.assertEqual(self.emp_1.fullname, 'Bob Smith')
        self.assertEqual(self.emp_2.fullname, 'Amy Williams')

        # change Employee objects names
        self.emp_1.first = 'John'
        self.emp_2.last = 'Smith'

        # test Employee fullname method again
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Amy Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        # call Employee apply_raise method
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        # test Employee apply_raise method
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 78750)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Williams/June')
            self.assertEqual(schedule, 'Bad Response!')
            

if __name__ == '__main__':
    unittest.main()
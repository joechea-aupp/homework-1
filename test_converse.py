import unittest
from converse import currency_conversion

class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        # Setup code here (if required, replace the 'pass')
        pass

    def tearDown(self):
        # Teardown code here (if required, replace the 'pass')
        pass

    def test_default_case(self):
        # Your test case logic here (replace the example assertion below)
        # You may also rename this to any function in the form of 'test_your_test_name(self):'
        self.assertTrue(True)

    def test_current_conversion(self):
        self.assertEqual(currency_conversion('USD', 2), 8000)
        self.assertEqual(currency_conversion('usd', 3), 12000)
        self.assertEqual(currency_conversion('Yuan', 3), 1929)
        self.assertEqual(currency_conversion('batH', 2), 246)
        self.assertEqual(currency_conversion('Yen', 2), 'not found')
        self.assertEqual(currency_conversion('yuan', 'ab'), 'invalid amount')

if __name__ == '__main__':
    unittest.main()


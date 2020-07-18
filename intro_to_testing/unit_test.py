import unittest

from test_function_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    
    
    def test_first_last_name(self):

        formatted_name = get_formatted_name('jafar', 'sadik')
        self.assertEqual(formatted_name, 'Jafar Sadik') 

unittest.main()
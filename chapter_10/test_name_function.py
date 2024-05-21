import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('abel', 'morara')
        self.assertEqual(formatted_name, 'Abel Morara')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('cynthia', 'morara', 'wambui')
        self.assertEqual(formatted_name, 'Cynthia Wambui Morara')

unittest.main()

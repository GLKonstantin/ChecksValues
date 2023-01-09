import unittest
from check_module.check_utils import get_list_from_string


class TestFunction(unittest.TestCase):

    def test_get_list_from_string(self):
        with self.subTest('test string'):
            self.assertEqual(get_list_from_string('test string'), ['test', 'string'])
        with self.subTest('test, string'):
            self.assertEqual(get_list_from_string('test, string'), ['test', 'string'])
        with self.subTest('test; string'):
            self.assertEqual(get_list_from_string('test; string'), ['test', 'string'])
        with self.subTest('test string,'):
            self.assertEqual(get_list_from_string('test string,'), ['test', 'string'])
        with self.subTest('test string;'):
            self.assertEqual(get_list_from_string('test string;'), ['test', 'string'])
        with self.subTest('test string, '):
            self.assertEqual(get_list_from_string('test string, '), ['test', 'string'])
        with self.subTest('test string; '):
            self.assertEqual(get_list_from_string('test string; '), ['test', 'string'])
        with self.subTest('test string,;'):
            self.assertEqual(get_list_from_string('test string,;'), ['test', 'string'])
        with self.subTest('test string,; '):
            self.assertEqual(get_list_from_string('test string,; '), ['test', 'string'])
        with self.subTest('test string,; '):
            self.assertEqual(get_list_from_string('test string,; '), ['test', 'string'])
        with self.subTest('test string,; '):
            self.assertEqual(get_list_from_string('test string,; '), ['test', 'string'])

        self.assertEqual(get_list_from_string('1,2,3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1;2;3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1,2;3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1;2,3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1, 2, 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1; 2; 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1, 2; 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1; 2, 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1, 2, 3 '), ['1', '2', '3'])
        self.assertEqual(get_list_from_string(' 1; 2; 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string(' 1, 2; 3'), ['1', '2', '3'])
        self.assertEqual(get_list_from_string(' 1; 2, 3 '), ['1', '2', '3'])
        self.assertEqual(get_list_from_string('1,2,3,4,5,6,7,8,9,10'), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.assertEqual(
            ['TestString', 'TestString'],
            get_list_from_string('TestString, TestString'),
        )
        self.assertEqual(
            ['TestString', 'TestString'],
            get_list_from_string('TestString; TestString'),
        )
        self.assertEqual(
            ['TestString', 'TestString'],
            get_list_from_string('TestString TestString'),
        )
        self.assertEqual(
            ['TestString', 'TestString'],
            get_list_from_string('TestString, TestString'),
        )

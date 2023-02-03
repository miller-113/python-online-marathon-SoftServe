"""Create function file_parser. If function is called with 2 arguments it
must count the number of occurrences string in a file, in case of 3 arguments
it must replace string in a file to new string

first argument - path to file

second argument - find string

third argument - replace string

Function must returned string with count of occurrences or count of replaced
strings

Example:

file_parser("file.txt", 'x', 'o')-> Replaced 8 strings file_parser(
"file.txt", 'o') -> Found 8 strings Please, create class ParsesTest and write
unittest for file_parser function uses mock object"""

# with open('path_to_file', 'w') as w_file:
import re
from unittest import mock
import unittest
from unittest.mock import patch, mock_open, Mock


def file_parser(path_to_file, string, replace=None):
    with open(path_to_file) as f:
        s = f.read()
        res = s.count(string)
        if not replace:
            return f'Found {res} strings'
        else:
            s.replace(string, replace)
            return f'Replaced {res} strings'



class ParserTest(unittest.TestCase):

    # def setUp(self):
    #     self.mok = mock.Mock(file="hello.txt")
    #     self.mok_f = mock.Mock()
    #     # self.mok.open.return_value.
    #     self.mok_f.file_parcer.return_value = "Replaced 5 strings"

    # @patch('__main__.open')
    def test_file_with_mock(self):
        with patch('builtins.open', mock_open(read_data='the test string for the test task')):
            actual = file_parser('parser.txt', 'test')
            expected = 'Found 2 strings'
            self.assertEqual(expected, actual)

    @patch('builtins.open', mock_open(read_data='the test string for the test task'))
    def test_file_with_mock1(self):
        # with patch('builtins.open', mock_open():
        actual = file_parser('parser.txt', 'test')
        expected = 'Found 2 strings'
        self.assertEqual(expected, actual)

    # @patch('builtins.open', mock_open(read_data='the test string for the test task'))
    # def test_file_with_mock2(self):
    #     mok = Mock(file="hello.txt")
    #     mok.return_value = ''
    #     self.assertEqual(mock_obj(), 'Found 8 strings')
        # with patch('builtins.open', mock_open():
        # actual = file_parser('parser.txt', 'test')
        # expected = 'Found 2 strings'
        # self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
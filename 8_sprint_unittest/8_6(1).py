import unittest
from unittest.mock import Mock
from unittest.mock import patch, mock_open


def file_parser(file, search_letter, replased_letter=None):
    if not file:
        raise FileNotFoundError

    f = open(file, "r")
    text = f.read()
    if replased_letter:
        count = text.count(search_letter)
        text = text.replace(search_letter, replased_letter)
        f.close()
        fw = open(file, 'w')
        fw.write(text)
        fw.close()
        return f"Replaced {count} strings"
    if not replased_letter:
        count = text.count(search_letter)
        return f"Found {count} strings"
    f.close()


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.mok = Mock(file="hello.txt")
        self.mok_f = Mock()
        self.mok_f.file_parcer.return_value = "Replaced 5 strings"

    @unittest.expectedFailure
    def test_read_file(self):
        self.assertFalse(file_parser(self.mok.file, 'eng'))

    def test_func_return(self):
        expected = "Replaced 5 strings"
        expected2 = 1
        self.assertEqual(expected, self.mok_f.file_parcer("1.txt", "txt", "open"))
        self.assertEqual(expected2, self.mok_f.file_parcer.call_count)

    def test_number_of_call_count(self):
        expected = 0
        self.assertEqual(expected, self.mok_f.file_parcer.call_count)

    # Emulating built in function open.read
    def test_get_file(self):
        with patch("builtins.open", mock_open(read_data="data")):
            expected = "Replaced 2 strings"
            self.assertEqual(expected, file_parser("1.txt", "a", "o"))

    def tearDown(self):
        self.mok = None
        self.mok_f = None
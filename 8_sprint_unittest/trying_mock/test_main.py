import unittest
from unittest.mock import patch, Mock, MagicMock

import requests
from requests.exceptions import Timeout
from main import len_jokes, get_joke


class TestJokes(unittest.TestCase):

    # @patch('main.get_joke')
    # def test_len_jokes(self, mock_obj):
    #     mock_obj.return_value = 'four'
    #     self.assertEqual(len_jokes(), 3)

    # @patch('main.requests')
    # def test_get_joke(self, mock_requests):
    #
    #     mock_response = MagicMock()
    #     mock_response.status_code = 401
    #     mock_response.json.return_value = {'value': 'hello there'}
    #     mock_requests.get.return_value = mock_response
    #     self.assertEqual(get_joke(), 'hello there')

    @patch('main.requests')
    def test_get_joke_raises_timeout_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        # mock_requests.get.side_effect = ConnectionError('Conn err msg')
        mock_requests.get.side_effect = Timeout('Test msg')
        self.assertEqual(get_joke(), 'No jokes, timeout server conn')
        # self.assertEqual(get_joke(), 'No jokes, timeout server conn')

    @patch('main.requests')
    def test_get_joke_raise_for_status_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions

        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = requests.exceptions.\
            HTTPError('Smth goes wrong')

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'HTTP error')


if __name__ == '__main__':
    unittest.main()
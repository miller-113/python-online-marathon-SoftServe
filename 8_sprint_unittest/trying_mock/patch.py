import unittest
# from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch, Mock
import requests
from datetime import datetime


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    @patch(f'{__name__}.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


class TestCalendarContextManager(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch(f'{__name__}.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


class TestCalendarPatch(unittest.TestCase):
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()


# class TestCalendarPatch1(unittest.TestCase):
#     @patch(f'{__name__}.requests')
#     def test_get_holidays_timeout(self, mock_requests):
#         mock_requests.side_effect = requests
#         response = mock_requests
#         response.status_code = 200
#         response.json.return_value = {'first': 1, 'second': 2}
#         mock_requests.get.return_value = response
#         self.assertEqual(get_holidays()['second'], 2)


class TestCalendarPatch1(unittest.TestCase):
    @patch(f'{__name__}.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.side_effect = requests
        response = mock_requests
        response.status_code = 200
        response.json.return_value = {'first': 1, 'second': 2}
        mock_requests.get.side_effect = [response]
        self.assertEqual(get_holidays()['second'], 2)


if __name__ == '__main__':
    unittest.main()

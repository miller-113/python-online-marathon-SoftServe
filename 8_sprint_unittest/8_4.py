import unittest


class TriangleNotValidArgumentException(Exception):
    def __init__(self, data):
        self.data = data


class TriangleNotExistException(Exception):
    def __init__(self, data):
        self.data = data


class Triangle:

    def __init__(self, data):
        self.data = data
        self.get_area()

    def get_area(self):
        try:
            a, b, c = self.data
            s = (a + b + c) / 2
            area = ((s * (s - a) * (s - b) * (s - c)) ** 0.5)
        except (TypeError, IndexError, ValueError):
            raise TriangleNotValidArgumentException('Not valid arguments')
        if isinstance(area, complex) or area == 0 or a < 1 or b < 1 or c < 1:
            raise TriangleNotExistException(
                'Can`t create triangle with this arguments')
        return area * 100 // 1 / 100


class TriangleTest(unittest.TestCase):

    def test_triangle_valid(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for item in valid_test_data:
            with self.subTest(item):
                triangle = Triangle(item[0])
                self.assertEqual(triangle.get_area(), item[1])

    def test_not_valid_triangle(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for item in not_valid_triangle:
            with self.subTest(f'{item}'):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(item).get_area()

    def test_not_valid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        for item in not_valid_arguments:
            with self.subTest(item):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(item).get_area()

# if __name__ == '__main__':
#     main()
# valid_test_data = [
#     (3, 4, 5),
#     (26, 25, 3),
#     (30, 29, 5),
#     (87, 55, 34),
#     (120, 109, 13),
#     (123, 122, 5)
# ]
# for data in valid_test_data:
#     print(Triangle(data).get_area())

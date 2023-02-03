"""Create class Worker with fields name and salary. If salary negative raise
ValueError

Create a method get_tax_value() that calculate tax from salary . Tax must be
calculate like "progressive tax" with next step:

less then 1000 - 0% 1001 - 3000 - 10% 3001 - 5000 - 15% 5001 - 10000 - 21%
10001 - 20000 - 30% 20001 - 50000 - 40% more than 50000 - 47% Please create
WorkerTest class with unitest to the class Worker. Try to use setUp and
tearDown methods. Don`t use assertRaises in tests.
"""

import unittest


class Worker:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary < 0:
            raise ValueError
        taxes_dict = {
            '1001-3000': 0.1,
            '3001-5000': 0.15,
            '5001-10000': 0.21,
            '10001-20000': 0.3,
            '20001-50000': 0.4,
            '50000': 0.47,
        }
        res = 0.0
        for k, v in taxes_dict.items():
            k = k.split('-')
            if k[0] == '50000' and self.salary > 50000:
                res += (self.salary - 50000) * 0.47
            elif self.salary in range(int(k[0])-1, int(k[1])):
                res += (self.salary - int(k[0])+1) * v
                break

            elif int(k[0]) < self.salary and len(k) > 1:
                res += (int(k[1])+1 - int(k[0])) * v

            else:
                break

        return res

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError
        self.salary = salary


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Vasia')

    def tearDown(self):
        del self.worker


    def test_tax_func_30_taxes(self):
        self.worker.set_salary(15000)
        self.assertEqual(self.worker.get_tax_value(), 3050)

    def test_tax_func_10_taxes(self):
        self.worker.set_salary(1500)
        self.assertEqual(self.worker.get_tax_value(), 50)

    def test_tax_func_0_taxes(self):
        self.worker.set_salary(500)
        self.assertEqual(self.worker.get_tax_value(), 0)

    def test_tax_func_15_taxes(self):
        self.worker.set_salary(4500)
        self.assertEqual(self.worker.get_tax_value(), 425)

    def test_tax_func_21_taxes(self):
        self.assertEqual(Worker('Alan', 8000).get_tax_value(), 1130)

    @unittest.expectedFailure
    def test_value_error(self):
        Worker('Alan', -222).get_tax_value()

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


# worker = Worker("Vika", 100000)
# print(worker.get_tax_value())
if __name__ == '__main__':
    unittest.main()
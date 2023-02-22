

# TASK 1

import unittest
from unittest import main

"""
Write the programm that calculate total price with discount by the products.

Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

Discount depends on count product:


count	discount
at least 5	5%
at least 7	10%
at least 10	20%
at least 20	30%
more than 20	50%
Write unittest with class CartTest and test all methods with logic
"""

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products):
        self.products = products

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        result = []

        for product in self.products:
            counts = product.count
            product = product.price * counts
            if 5 <= counts < 7:
                product -= product/20
            elif 7 <= counts < 10:
                product -= product/10
            elif 10 <= counts < 20:
                product -= product / 5
            elif counts == 20:
                product -= product * 0.3
            elif counts > 20:
                product -= product/2
            result.append(product)
        return sum(result)


class CartTest(unittest.TestCase):
    tests_products = (Product('p1', 10, 4),
    Product('p2', 100, 5),
    Product('p4', 300, 6),
    Product('p5', 400, 9),
    Product('p6', 500, 10),
    Product('p7', 500, 23),
    Product('p8', 1000, 20))

    # def test_raise_error(self):
    #     with self.assertRaises(TypeError):
    #         return 0

    def test_discount(self):
        self.assertEqual(Cart((self.tests_products[1],
                              self.tests_products[2])).get_total_price(), 2185)


if __name__ == '__main__':
    # main()
    products = (Product('p1',10,4),
    Product('p2',100,5),
    Product('p3',200,6),
    Product('p4',300,7),
    Product('p5',400,9),
    Product('p6',500,10),
    Product('p7',1000,20))
    cart = Cart(products)
    print(cart.get_total_price())
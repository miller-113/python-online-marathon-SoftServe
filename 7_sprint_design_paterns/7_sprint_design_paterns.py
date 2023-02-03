"""You have to create a main course and a dessert at an Italian and a French
restaurant, but you won't mix one cuisine with the other.

Your task is:

1) define a class Product with an abstract method cook(). This class would be
base class for the next classes:

- class FettuccineAlfredo with field name ("Fettuccine Alfredo"), method
cook() provides an output of the formatted string "Italian main course
prepared: " and name of the dish;

 - class Tiramisu, with field name ("Tiramisu"), method cook() provides an
 output of the formatted string "Italian dessert prepared:" and name of the
 dish;

- class DuckALOrange, with field name ("Duck À L'Orange"), method cook()
provides an output of the formatted string "French main course prepared: "
and name of the dish;

- class CremeBrulee,  with field name ("Crème brûlée"), method cook()
provides an output of the formatted string "French dessert prepared: " and
name of the dish.

2) define a class Factory with an abstract method get_dish() that takes
type_of_meal as a parameter. This class would be base class for the classes
ItalianDishesFactory and FrenchDishesFactory. The method get_dish() according
to type_of_meal ("main" or "dessert") invokes the dish of appropriate cousine;

3) define a class FactoryProducer with the method get_factory(). The method
takes the parameter type_of_factory and invokes the appropriate dishes
factory (classes ItalianDishesFactory or FrenchDishesFactory). """

# TASK 1 - FACTORY

# import abc
# from abc import ABC
#
#
# class FactoryProducer:
#
#     def get_factory(self, type_of_factory):
#         if type_of_factory == 'italian':
#             return ItalianDishesFactory()
#         return FrenchDishesFactory()
#
#
# class Factory:
#
#     @abc.abstractmethod
#     def get_dish(self, type_of_meal):
#         pass
#
#
# class ItalianDishesFactory(Factory):
#     def get_dish(self, type_of_meal):
#         if type_of_meal == 'main':
#             return FettuccineAlfredo
#         return Tiramisu
#
#
# class FrenchDishesFactory(Factory):
#     def get_dish(self, type_of_meal):
#         if type_of_meal == 'main':
#             return DuckALOrange
#         return CremeBrulee
#
#
# class Product(abc.ABC):
#
#     @abc.abstractmethod
#     def cook(self):
#         pass
#
#
# class FettuccineAlfredo(Product):
#
#     @staticmethod
#     def cook():
#         dish = "Fettuccine Alfredo"
#         print(f"Italian main course prepared: {dish}")
#
#
# class Tiramisu(Product):
#
#     @staticmethod
#     def cook():
#         dish = "Tiramisu"
#         print(f"Italian dessert prepared: {dish}")
#
#
# class DuckALOrange(Product):
#
#     @staticmethod
#     def cook():
#         dish = "Duck À L'Orange"
#         print(f"French main course prepared: {dish}")
#
#
# class CremeBrulee(Product):
#
#     @staticmethod
#     def cook():
#         dish = "Crème brûlée"
#         print(f"French dessert prepared: {dish}")
#
#
#
# fp = FactoryProducer()
# fac = fp.get_factory("italian")
# main_dish = fac.get_dish("main")
# main_dish.cook()

# END TASK

"""Your task is to create an application for the departmental store. 
Initially, there was one and only one type of discount called the 
On-Sale-Discount (50%). But as time passes, the owner of the departmental 
store demands for including some other types of discount also for the 
customers. 

Please, solve the above-described problem in an efficient way. Our actual 
class should store the reference to one of the strategy function. 

You have the structure of your future application in the answer box preload.
"""

# TASK 2

# class Goods:
#     s = 'Customer'
#     def __init__(self, price, discount_strategy=None):
#         self.price = price
#         self.discount_strategy = discount(self) if (discount := discount_strategy) else None
#
#     def price_after_discount(self):
#         return self.price - self.discount_strategy if self.discount_strategy else self.price
#
#     def __str__(self):
#         return f'Price: {self.price}, price after discount: {self.price_after_discount()}'
#
#
# def on_sale_discount(order):
#     return order.price / 2
#
#
# def twenty_percent_discount(order):
#     return order.price / 5
#
#
# print(Goods(20000))
# print(Goods(20000, discount_strategy=twenty_percent_discount))


# END TASK

"""Imagine you are creating an application that shows the data about all 
different types of vehicles present. It takes the data from APIs of different 
vehicle organizations in XML format and then displays the information. But 
suppose at some time you want to upgrade your application with a Machine 
Learning algorithms that work beautifully on the data and fetch the important 
data only. But there is a problem, it takes data in JSON format only. It will 
be a really poor approach to make changes in Machine Learning Algorithm so 
that it will take data in XML format. 

For solving the problem we defined above, you can use Adapter Method that 
helps by creating an Adapter object. To use an adapter in your code: 

Client should make a request to the adapter by calling a method on it using 
the target interface. Using the Adaptee interface, the Adapter should 
translate that request on the adaptee. Result of the call is received the 
client and he/she is unaware of the presence of the Adapter’s presence. Class 
diagram for the Adapter method: Adapter-class-diagram1.png in img"""
# TASK 3

#
# class MotorCycle:
#
#     """Class for MotorCycle"""
#
#     def __init__(self):
#         self.name = "MotorCycle"
#         self.wheels = self.two_wheeler
#
#     @staticmethod
#     def two_wheeler():
#         return "TwoWheeler"
#
#
# class Truck:
#     """Class for Truck"""
#
#     def __init__(self):
#         self.name = "Truck"
#         self.wheels = self.eight_wheeler
#
#     @staticmethod
#     def eight_wheeler():
#         return "EightWheeler"
#
#
# class Car:
#     """Class for Car"""
#
#     def __init__(self):
#         self.name = "Car"
#         self.wheels = self.four_wheeler
#
#     @staticmethod
#     def four_wheeler():
#         return "FourWheeler"
#
#
# class Service(Car, Truck, MotorCycle):
#     pass
#
#
# class Adapter(Service):
#     """
#     Adapts an object by replacing methods.
#     Usage:
#     motorCycle = MotorCycle()
#     motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
#     """
#
#     def __init__(self, obj, **adapted_methods):
#         # super().__init__()
#         self.obj = obj
#         self.adapted_methods = adapted_methods
#         """We set the adapted methods in the object's dict"""
#
#     def __getattr__(self, attr):
#         """All non-adapted calls are passed to the object"""
#         return getattr(self.obj, attr)
#
#     def original_dict(self):
#         """Print original object dict"""
#         return self.__dict__
#
#
# objects = []
# motorCycle = MotorCycle()
# objects.append(Adapter(motorCycle, wheels=motorCycle.two_wheeler))
# truck = Truck()
# objects.append(Adapter(truck, wheels=truck.eight_wheeler))
# car = Car()
# objects.append(Adapter(car, wheels=car.four_wheeler))
# for obj in objects:
#     print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

# END TASK

"""Imagine we have a washing machine which can wash the clothes, rinse the 
clothes and spin the clothes but all the tasks separately. We need a system 
that can automate the whole task without the disturbance or interference of us. 

To solve the above-described problem, we would like to hire the Facade 
Method. It will help us to hide or abstract the complexities of the 
subsystems as follows. Facade-method-class-diagram.png in img"""

# TASK 4


# class WashingMachine:
#
#     def startWashing(self):
#         Washing.wash()
#         Rinsing.rinse()
#         Spinning.spin()
#
#     def method1(self):
#         pass
#
#
# class Washing:
#     @staticmethod
#     def wash():
#         print('Washing...')
#
#
# class Rinsing:
#     @staticmethod
#     def rinse():
#         print('Rinsing...')
#
#
# class Spinning:
#     @staticmethod
#     def spin():
#         print('Spinning...')
#
#
# washingMachine = WashingMachine()
# washingMachine.startWashing()

# END TASK

import abc
from typing import List


class CompositeElement:

    def __init__(self, *args):
        self._data = args[0]
        # self._children = [*args] if args else []
        self._children = []
        '''Takes the first positional argument and assigns to member
         variable "position". Initializes a list of children elements.'''

    def add(self, child):
        '''Adds the supplied child element to the list of children
         elements "children".'''

        self._children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of
        children elements "children".'''
        return self._children.remove(child)

    def showDetails(self):
        '''Prints the details of the component element first. Then,
        iterates over each of its children, prints their details by
        calling their showDetails() method.'''
        print(self._data)
        for child in self._children:
            print("\t", end="")
            child.showDetails()


class LeafElement:

    def __init__(self, *args):
        ''''Takes the first positional argument and assigns to member
         variable "position".'''
        self._data = args[0]


    def showDetails(self):
        print("\t", end ="")
        print(self._data)


topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()

# TASK1
# class Employee:
#
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#
#     @staticmethod
#     def from_string(string):
#         string = string.split('-')
#         return Employee(string[0], string[1], int(string[2]))
#
#
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# t = 'John-Smith-55000'


# END TASK1

# _________________________________________________________
# _________________________________________________________
# _________________________________________________________

# _________________________________________________________
# Create a Pizza class with the attributes order_number and ingredients
# (which is given as a list).
# Only the ingredients will be given as input.
#
# You should also make it so that its possible to choose a ready-made pizza
# flavour rather than typing
# out the ingredients manually! As well as creating this Pizza class, hard-code
# the following pizza flavours.
#
# S6_2
#
# Examples:
# p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2
# _________________________________________________________
# TASK2


# class Pizza:
#     order_number = 0
#
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#         Pizza.order_number += 1
#         self.order_number = Pizza.order_number
#
#     @staticmethod
#     def hawaiian():
#         return Pizza(['ham', 'pineapple'])
#
#
# p = Pizza(['ham'])
# # p1 = Pizza.hawaiian()
# print(p.order_number)
#
#
# p1 = Pizza(['bacon', 'parmesan', 'ham'])
# print(p1.order_number)
# print(Pizza.__bases__)

# END TASK2
# _________________________________________________________
# _________________________________________________________
# _________________________________________________________

# _________________________________________________________

# Create a class Employee that will take a full name as argument, as well as
# a set of none, one or more keywords.
#
# Each instance should have a name and a lastname attributes plus one more
# attribute for each of the keywords, if any.
#
# Examples: john = Employee("John Doe") mary = Employee("Mary Major",
# salary=120000) richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182,
# nationality="Italian") mary.lastname ➞ "Major" richard.height ➞ 178
# giancarlo.nationality ➞ "Italian" john.name ➞ "John"

# _________________________________________________________

# TASK3


# class Employee:
#     def __init__(self, full_name, **keywords):
#         self.full_name = full_name
#         self.name = full_name.split(' ')[0]
#         self.lastname = full_name.split(' ')[1]
#         self.salary = keywords.get('salary', 0)
#         self.height = keywords.get('height', 0)
#         self.nationality = keywords.get('nationality', '')
#         self.subordinates = keywords.get('subordinates', [])
#
#
# john = Employee("John Doe") mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178) giancarlo =
# Employee("Giancarlo Rossi", salary=115000, height=182,
# nationality="Italian") # mary.lastname # richard.height #
# giancarlo.nationality # john.name print(giancarlo.name) print(
# giancarlo.nationality)

# END TASK3

# _________________________________________________________
# _________________________________________________________
# _________________________________________________________

# Your task is to write a program which allows teachers to create a multiple
# choice test in a class called Test-paper and to be also able to assign a
# minimum pass mark. The test paper's subject should also be included. The
# attributes are in the following order:
#
# 1. subject 2. mark-scheme 3. pass_mark As well as that, we need to create
# student objects to take the test itself! Create another class called
# Student and do the following:
#
# Create an attribute called tests_taken and set the default as  'No tests
# taken'. Make a method called take_test(), which takes in the test-paper
# object they are completing and the student's answers. Compare what they
# wrote to the mark scheme, and append to the/create a dictionary assigned to
# tests_taken in the way as shown in the point below. Each key in the
# dictionary should be the test-paper subject and each value should be a
# string in the format seen in the examples below (whether the student has
# failed, and their percentage in brackets). Example:
#
# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%") paper2 =
# Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%") paper3 = Testpaper(
# "Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
#
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ "No tests taken"
# student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
# student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
#
# student2.take_test(paper2, ["1C", "2D", "3A", "4C"]) student2.take_test(
# paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"]) student2.tests_taken ➞
# {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

# TASK 4

# class Testpaper:
#     def __init__(self, subject, markscheme, pass_mark):
#         self.subject = subject
#         self.markscheme = markscheme
#         self.pass_mark = pass_mark
#
#
# class Student:
#     def __init__(self, test_taken='No tests taken'):
#         self.tests_taken = test_taken
#
#     def take_test(self, test_paper_obj, marks):
#         correct_marks = test_paper_obj.markscheme
#         answered_correct_m = len(
#             [student_m for student_m in marks for answer in correct_marks if
#              student_m == answer])
#
#         score = int(round(100 / len(correct_marks) * answered_correct_m, 0))
#         is_passed = int(test_paper_obj.pass_mark.split('%')[0]) <= score
#         result = {test_paper_obj.subject:
#                   f'Passed! ({score}%)' if is_passed else
#                   f'Failed! ({score}%)'
#                   }
#
#         self.tests_taken = result if isinstance(self.tests_taken, str) \
#             else {**self.tests_taken, **result}

# END TASK

# paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
# paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'],
#                    '75%')

# student2 = Student()
# student3 = Student()
# # student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
# print(student3.tests_taken)
# student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
# print(student3.tests_taken)
# student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
# print(student3.tests_taken)
# print(paper3.subject)
# print(paper3.markscheme)
# print(paper3.pass_mark)

# _________________________________________
# _________________________________________
# _________________________________________

# The basic premise of the game Gallows is to follow two rules:
#
# First character of next word must match last character of previous word.
# The word must not have already been said.
# Below is an example of a Gallows game:
#
# ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!
#
# ['motive', 'beach']  # invalid! - beach should start with "e"
#
# ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
# Write a Gallows class that has two instance variables:
#
# words: a list of words already said.
# game_over: a boolean that is true if the game is over.
# and two instance methods:
#
# play: a method that takes in a word as an argument and checks if it is
# valid (the word should follow rules #1 and #2 above).
#
# If it is valid, it adds the word to the words list, and returns the words
# list. If it is invalid (either rule is broken), it returns "game over" and
# sets the game_over boolean to true. restart: a method that sets the words
# list to an empty one [] and sets the game_over boolean to false. It should
# return "game restarted".
#
# Examples:
# my_gallows = Gallows()
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# # Words should be accessible.
# my_gallows.restart() ➞ "game restarted"
# # Words list should be set back to empty.
# my_gallows.play('hostess') ➞ ['hostess']
# my_gallows.play('stash') ➞ ['hostess', 'stash']
# my_gallows.play('hostess') ➞ "game over"
# # Words cannot have already been said.
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# # Corn does not start with an "o".
# my_gallows.play('corn') ➞"game over"
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# my_gallows.restart() ➞ "game restarted"
# my_gallows.words ➞ []

# TASK5

# class Gallows:
#     def __init__(self):
#         self.words = []
#         self.game_over = False
#
#     def play(self, word):
#         if not self.words:
#             self.words.append(word)
#             return self.words
#         elif word not in self.words and word[0] == self.words[-1][-1]:
#             self.words.append(word)
#             return self.words
#         else:
#             self.game_over = True
#             return "game over"
#
#     def restart(self):
#         self.game_over = False
#         self.words = []
#         return "game restarted"


# my_gallows = Gallows()
# print(my_gallows.game_over)
# print(my_gallows.play('apple'))
# print(my_gallows.words)
# print(my_gallows.play('ear'))
# print(my_gallows.play('rhino'))
# print(my_gallows.play('ocelot'))
# print(my_gallows.game_over)
# print(my_gallows.play('oops'))
# print(my_gallows.game_over)
# print(my_gallows.words)

# END TASK

# ___________________________________________________________

# Example with using __new__
# class A:
#     c_str = 'empty'
#     c_lst = []
#
#     def __new__(cls, *args, **kwargs):
#         inst = super(A, cls).__new__(cls)
#         inst.a = {1: '1', 2: '2'}
#         return inst
#
#     def __init__(self, srting):
#         self.i_str = srting
#         self.i_lst = [1, 2, 3]
#
#
# # a = A()
# b = A('test')
# b.c_lst.append(2334)
# # print(a.c_lst)
# # print(b.c_lst)
# Another one with __new__
# class Singleton:
#     obg = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.obg is None:
#             # cls.obg = super(Singleton, cls).__new__(cls)
#             cls.obg = object.__new__(cls)
#
#             print(cls.obg)
#             cls.obg.a = {1: '1', 2: '2'}
#         return cls.obg
#
#     def __init__(self, *args, **kwargs):
#         print(*args, **kwargs)
#
#
# s1 = Singleton('way')
# s2 = Singleton('day')
# ___________________________________________________________

class A:
    def __init__(self):
        self.cal(30)
        print('i form A is', self.i)

    def cal(self, i):
        self.i = 2 * i


class B(A):
    def __init__(self):
        super().__init__()
        print('i form B is', self.i)
        print(1)
        # self.cal(30)

    def cal(self, i):
        self.i = 3 * i


b = B()


# ___________________________________________________________
#
#     TOTAL_OBJECTS=0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS+1
#
#     # @classmethod
#     # def total_objects(cls):
#     #     print("Total objects: ", cls.TOTAL_OBJECTS)
# # Создаем объекты родительского класса
# my_obj1 = MyClass()
# print(dir(MyClass))
#
# my_obj2 = MyClass()
# print(MyClass.mro())
# # Создаем дочерний класс
# class ChildClass(MyClass):
#     TOTAL_OBJECTS=0
#     pass
#
#
# print(ChildClass.mro())
# print(ChildClass.__mro__)

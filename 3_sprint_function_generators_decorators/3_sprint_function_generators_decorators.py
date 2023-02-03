# Create function with name outer(name). This function should return inner
# function with name inner.
# This inner function prints message Hello, <name>!
# For example
# tom = outer("tom")
# tom() -> Hello, tom!

# TASK1
# from typing import Callable
#
#
# def outer(name: str) -> Callable[[], None]:
#     def inner():
#         print(f'Hello, {name}!')
#
#     return inner
#
#
# # tom = outer('Nick')
# # print(tom)
# alice = outer("Alice")
# alice()
# END TASK

# _________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________


# Create_ function create with one string argument. This function should return
# anonymous function that checks if the
# argument of function is equals to the argument of outer function.
#
# For example:
#
#  tom = create("pass_for_Tom")
#
#  tom("pass_for_Tom") returns true
#
#  tom("pass_for_tom") returns false

# TASK2
# from typing import Callable, Any
#
#
# def create(arg: str) -> Callable[[Any], bool]:
#     def inner(next_arg=' '):
#         return True if arg == next_arg else False
#
#     return inner
#
#
# def create1(arg: str) -> Callable[[Any], bool]:
#     return lambda x: True if arg == x else False
#
#
# tom = create("pass_for_Tom")
#
# tom("pass_for_Tom")
#
# tom("pass_for_tom")
# END TASK

# ______________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________


# Create_ function
# create_account(user_name: string, password: string, secret_words: list).
# This function should
# return inner function check.
# The function check compares the values of its arguments with password
# and secret_words:
#  the password must match completely, secret_words may be misspelled
#  (just one element).
# Password should contain at least 6 symbols including one uppercase letter,
# one lowercase letter,  special character
# and one number.
#
# Otherwise, function create_account raises ValueError.
#
# For example:
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"]) then
# tom("Qwerty1_",  ["1", "word"]) return True
# tom("Qwerty1_",  ["word"]) return False due to different length of
# ["1", "word"] and  ["word"]
# tom("Qwerty1_",  ["word", "12"]) return True
# tom("Qwerty1!",  ["word", "1"]) return False
# because "Qwerty1!" not equals to "Qwerty1_"
# _______________________________________________________________________

# TASK3

# from string import punctuation
#
#
# def create_account(user_name: str, password: str, secret_words: list):
#     if len(password) < 6 or not any(val.islower() for val in password) \
#             or not any(val.isupper() for val in password) \
#             or not any(val.isdigit() for val in password) \
#             or not any(True for sym in set(punctuation) if sym in password):
#         print("Raises ValueError")
#
#     def check(password2: str, secret_words2: list):
#         length = len(secret_words)
#
#         check_secret = len([secret_words[i] for i in range(length) \
#               if secret_words[i] in secret_words2])
#         counter = 0
#         counter1 = 0
#
#         for i in set(secret_words):
#             if i in set(secret_words2):
#                 counter += 1
#             if secret_words2.count(i):
#                 counter += secret_words2.count(i) - 1
#         for i in set(secret_words2):
#             if i in set(secret_words):
#                 counter1 += 1
#             if secret_words.count(i):
#                 counter1 += secret_words.count(i) - 1
#
#         if password == password2 \
#                 and length == len(secret_words2) \
#                 and length - 1 <= counter <= length + 1 \
#                 and length - 1 <= check_secret <= length + 1:
#             return True
#         return False
#
#     return check
#
#
# # checked_arr_6_true = ["1", "word"]
# # val1 = create_account("123", "qQ1!45", ["1", "word"])
# # print(val1("qQ1!45", checked_arr_6_true))
#
# tom = create_account("Tom", "Qwerty1_", ['1', '2', '1'])
# check1 = tom("Qwerty1_", ['1', '1', '4'])


# check2 = tom("Qwerty1_", ["word"])
# check3 = tom("Qwerty1_", ["word", "2"])
# check4 = tom("Qwerty1!", ["word", "12"])
# a = ['1', '2', '1']
# b = ['1', '1', '4']

# END TASK

# ________________________________________________________________________
# ________________________________________________________________________
# ________________________________________________________________________
# ________________________________________________________________________


# Create function-generator divisor that should return all
# divisors of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

# TASK4

# def divisor(num):
#     # for i in range(1, num + 1):
#     i = 0
#     while True:
#         i += 1
#         if i <= num:
#             if num % i == 0:
#                 yield i
#         else:
#             yield None
#
#
# two = divisor(2)
# print(next(two))
# print(next(two))
# print(next(two))
# print(dir(divisor(2)))


# def curry(callback):
#
#     def b(name:str):
#         def c(greet: str):
#             callback(name, greet)
#         return c
#     return b
#
# def greeting(word, name):
#     print(f'{word}, {name}')
#
# print(curry('nick')('jak'))

# END TASK


# ________________________________________________________________________
# ________________________________________________________________________
# ________________________________________________________________________

# Create decorator logger. The decorator should print to the console information
# about function's name
# and all its arguments separated with ',' for the function
# decorated with logger.
# Create function concat with any numbers of any arguments which concatenates
# arguments and apply logger decorator
# for this function.
# For example
# print(concat(2, 3)) display
# Executing of function concat with arguments 2, 3...
# 23
# print(concat('hello', 2)) display
# Executing of function concat with arguments hello, 2...
# hello2
#
# print(concat (first = 'one', second = 'two')) display
# Executing of function concat with arguments one, two...
# one two


# TASK 5

# def decorator(func):
#     def wrap(*args, **kwargs):
#         tmp = func(*args, **kwargs)
#         func_name = func.__name__
#         arguments = ', '.join([str(i) for i in [*args, *kwargs.values()]])
#         print(f'Executing of function {func_name} with {arguments}...')
#         return tmp
#     return wrap
#
#
# @decorator
# def concat(*args, **kwargs):
#     return ''.join([str(i) for i in [*args, *kwargs.values()]])
#
#
# # print(concat('22', 334))
# print(concat('first string', second = 2, third = 'second string'))

# @decorator
# def my_func(name, greeting):
#     return f'{name}, {greeting}'
# print(my_func(name='NIck', greeting='hi everyone'))

# @decorator
# def sub(a, b):
#     return a - b

# print(sub(2, 3))

# END TASK


# _____________________________________________________________________
# _____________________________________________________________________
# _____________________________________________________________________

# from random import randint


# Generator function randomWord has as an argument list of words.
# It should return any random word from this list.
#  Each time words are different until the end of the list is reached.
#  Then words are taken from the initial list again.
#
#
# For example if
#
# list = ['book', 'apple', 'word']
#
# books = randomWord(list)
#
# then possible output example
#
# first call of next(books) returns apple
#
# second call of next(books) returns book
#
# third call of next(books) returns word
#
# fourth call of next(books) returns book
# ____________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________

# TASK6

# from random import randint
#
#
# def random_word(lst: list):
#     # print(lst)
#     # lst = set(lst)
#     counter = 0
#     while True:
#         if counter < len(lst):
#             yield lst[randint(0, len(lst)-1)]
#         elif len(lst) == 0:
#             yield None
#         else:
#             yield lst[counter % len(lst)]
#         counter += 1
#
#
# lst_ = ['book', 'apple', 'word']
#
# books = random_word(lst_)
#
# print(next(books))
# print(next(books))
# print(next(books))
# print(next(books))

# END TASK

_fib_cache = {1: 1, 2: 1}  # ключ - номер числа, значения - число фиб


# EXPERIMENTAL OR ADDITIONAL MATERIAL
# EXPERIMENTAL OR ADDITIONAL MATERIAL
# EXPERIMENTAL OR ADDITIONAL MATERIAL

# import datetime
#
#
# def clock(func):
#     start = datetime.datetime.now()
#     print(f'Time start: {start}')
#
#     def wrapp(*args, **kwargs):
#         temp = func(*args, *kwargs)
#         # print(temp)
#         return temp
#
#     print(f'Time stop: {datetime.datetime.now() - start}')
#
#     return wrapp

# ____________________________________________________________________________________________________________________

# @time.clock

# @clock
# def mem_fib(n):
#     result = _fib_cache.get(n)
#     if result is None:
#         result = mem_fib(n - 2) + mem_fib(n - 1)
#         _fib_cache[n] = result
#     return result


# print(dec(mem_fib)(18))
# ____________________________________________________________________________________________________________________


# # print(fib(20))
# # print(mem_fib(1500))
# def memoize(f):
#     cache = {}
#
#     def decorate(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             cache[args] = f(*args)
#             return cache[args]
#     return decorate
#
#
# @memoize
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)
#
# print('fib(20) =', fib(20))

# ____________________________________________________________________________________________________________________

# то же самое через lambda
# def memoize(f):
#     cache = {}
#     return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

# универсальный декоратор для любого количества аргументов
# def memoize(f):
#     cache = {}
#
#     def decorate(*args, **kwargs):
#         key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
#         if key not in cache:
#             cache[key] = f(*args, **kwargs)
#         return cache[key]
#
#     return decorate

# ____________________________________________________________________________________________________________________
# currying || partial application
# def greet_deeply_curried(greeting):
#     def w_separator(separator):
#         def w_emphasis(emphasis):
#             def w_name(name):
#                 print(greeting + separator + name + emphasis)
#
#             return w_name
#
#         return w_emphasis
#
#     return w_separator
#
#
# greet = greet_deeply_curried("Hello")("...")(".")
# greet('German')
# greet('Ivan')
#
# greet_deeply_lambda = lambda greeting: lambda separator: lambda name: lambda surname: print(f'{greeting}{separator}'
#                                                                                             f'{name} {surname}')
# greet_deeply_lambda('Guden Tak')(' _ ')('Nick')('Shkurat')
#
# print('center'.center(50, '-'))
#
# from functools import partial
#
#
# def greet(greeting, separator, emphasis, name):
#     print(greeting + separator + name + emphasis)
#
# newfunc = partial(greet, greeting='Hello', separator=',', emphasis='.')
# newfunc(name='German')
# newfunc(name='Ivan', separator='__')


# ____________________________________________________________________________________________________________________


# import functools
# import time
#
# def timer(func):
#     """Выводит время выполнения декорируемой функции"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Функция {func.__name__!r} выполнена за {run_time:.4f} с")
#         return value
#     return wrapper_timer
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])
#
#
# waste_some_time(222)


# class Even:
#     def __init__(self, max):
#         self.n = 2
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             result = self.n
#             self.n += 2
#             return result
#         else:
#             raise StopIteration
#
#
# numbers = Even(10)


# _____________________________________________
# _____________________________________________
# _____________________________________________
# ADDITIONAL



pandas = "Pandas"

def decorator(func):
    def wrapper(*args, **kwargs):
        print(''.join([arg.upper() for arg in args]))
        return func(*args, **kwargs)
    return wrapper


@decorator
def to_upper(*args):
    return args

print(to_upper('ghb dfg'))
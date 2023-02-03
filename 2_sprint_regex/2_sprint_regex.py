# Task1

# As input data, you have a list of strings.
# Write a method double_string() for counting the number of strings from the list, represented in the form of the concatenation of two strings from this arguments  list
# For example:
# Test	Result
# data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# print(double_string(data))
# 3
# data = ['aa', 'abc', 'qwerqwer']
# print(double_string(data))
# 0


# def double_string(data):
#     counter = 0
#     for i in range(len(data)):
#         counter += 1 if data[i] in [i + x for i in data for x in data] else 0
#     return counter
#
#
# # data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
# data_ = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
#
# print(double_string(data_))


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________

# Task2

# Numbers in the Morse code have the following pattern:
#
# all digits consist of 5 characters;
# the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
#
#
#
# Attention!
# Do not use any collection data like lists, tuples, dictionaries for holding Morse codes
#
# For example:
#
# Test	Result
# print(morse_number("295"))
# ..--- ----. .....
# print(morse_number("005"))
# ----- ----- .....
# print(morse_number("513"))
# ..... .---- ...--
# print(morse_number("784"))
# --... ---.. ....-


# def morse(numbers: str):
#     res = ''
#
#     for num in numbers:
#         num = int(num)
#         if num >= 5:
#             for i in range(1, 6):
#                 res += '.' if num < 6 else '-'
#                 num -= 1
#             res += ' '
#         else:
#             res += ''.join(['.' if i < num else '-' for i in range(5)]) + ' '
#     return res
#
#
# n = 3
# print(morse('295'))


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# Task3
"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:

!!!!Sprint_2-3_formula.png!!!!!

For example:

Test	Result
test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
10.0
test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
18.73454147995595
"""

# import re
# from math import pow, sqrt
#
#
# def perimetr(data):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, re.findall(r'\d+', data))
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 \
#         + ((x2 - x4) ** 2 + (y2 - y4) ** 2) ** 0.5 \
#         + ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5 \
#         + ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
#
#
# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(perimetr(test1))


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# Task4

'''As input data, you have a string that consists of words that have duplicated characters at the end of it.

All duplications may be in the next format:

wordxxxx
wordxyxyxy
wordxyzxyzxyz
, where x, xy or xyz repeated ending of the word

Using re module write function pretty_message() that remove all duplications

For example:

Test	Result
data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
This is echo string. Replace repeated groups of symbols
data = "Another input data string"
print(pretty_message(data))
Another input data string'''

# import re
# text = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# # prety_message = lambda x: re.sub(r'(\w{1}|\w{2}|\w{3})\1+', r'\1', x)
# # print(prety_message(text))
#
#
# def pretty_message(data):
#     return re.sub(r'(\w{1,3}?)\1+', r'\1', data)
#
#
# print(pretty_message(text))


# _____________________________________________________________________________________________________________________ 
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# Напишите выражение, которое найдет правильно написанные теги:
# <h2>Заголовок 2-ого уровня</h2>
# <h3>Заголовок 3-ого уровня</h3>
# Но не найдет ошибки:
# <h2>Заголовок 2-ого уровня</h3>
r'''^<(\w\d>)[А-я\s\d-]+<\/\1'''
"""
<h2>Заголовок 2-ого уровня</h2>
<h3>Заголовок 3-ого уровня</h3>
<h2>Заголовок 2-ого уровня</h3>
"""
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# Task5

'''
As input data you have list of strings with information about some location:

"id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"

Using regular expression write method max_population() for parsing strings and get info about location with highest population 

For example:

Test	Result
data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))
('eu_kyiv', 24834)

'''


# # "id,name,poppulation,is_capital",
# lst = ["3024,eu_kyiv,24834,y",
#        "3025,eu_volynia,25231,n",
#        "3026,eu_galych,23745,n",
#        "4892,me_medina,18038,n",
#        "4401,af_cairo,18946,y",
#        "4700,me_tabriz,13421,n",
#        "4899,me_bagdad,22723,y",
#        "600,af_zulu,09720,n"]
#
# # print(sorted(lst, ley=lambda x: x[0]))
# import re
# from functools import reduce
# city_and_population = list(map(lambda x: re.findall(r',([\w_]+),(\d+)', x), lst))
# sor = sorted(city_and_population, key=lambda x: x[0][1], reverse=True)
# sor1 = reduce(lambda a, z: a if a[1] > z[1] else z, [last for inner in city_and_population for last in inner])
#
#
# def max_population(data):
#     city_and_population = list(map(lambda x:
#                                    re.findall(r',([\w_]+),(\d+)', x), data))
#     res = reduce(lambda a, z: a if a[1] > z[1] else z,
#             [last for inner in city_and_population for last in inner])
#     return res[0], int(res[1])


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
'''ЗАМЕНА в RegEx'''
import re
s = '''
05.08.2015

01.01.1999

03.02.2000
'''
print(re.sub(r'(\d{2})\.(\d{2})\.(\d{4})', r'\3-\2-\1', s))

t = 'helolololo na na na privet ja tut' #hellollollo  hello'
print(re.sub(r'(.|..|...)\1+', r'\1', t))
print('NEXT'.center(50, '_'))
print(re.sub(r'(\w{1,3}?)\1+', r'\1', t))
print('NEXT'.center(50, '_'))
print('####'.center(50))
# замена повторов в слове. Только до 1
print(re.findall(r'(\w{1,4}?)\1+', t))
# замена повторов в словах и в строке. 1 и более
print(re.sub(r'([\w\s]{1,4}?)\1+', r'\1', t))

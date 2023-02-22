"""For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n, or sums of distinct powers of n.

Your task is to find the kth (1-based) number in this sequence.

Example

For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.

Input/Output

[input] integer n

The number to build the sequence by.

Constraints:
2 ≤ n ≤ 30.

[input] integer k

The 1-based index of the number in the sequence.

Constraints:
1 ≤ k ≤ 100.

[output] integer

The kth element of the sequence."""
# def kth_term(num, kth):
#     lst = []
#     for i in range(kth):
#         lst.append(n**i)
#         if num**i % num == 0:
#             for position in range(len(lst) - 1):
#                 if len(lst) > kth-1:
#                     break
#                 lst.append(num ** i + lst[position])
#     return lst[kth-1]
#
#
# print(kthTerm(30, 100))


# __________________________________________________________________________________________________
"""John wants to filter all the verses in a specific chapter in the Bible by the verse id. The Bible has 66 books, each book has a lot of chapters, and each chapter has a lot of verses.

The pattern of the id is bbcccvvv, where:

bb is the Book ID. (01 < bb ≤ 66);
ccc is the Chapter ID. (001 ≤ ccc);
vvv is the Verse ID. (001 ≤ vvv).
John wants to find verses that belong to the Book and Chapter, given by their IDs.

Example:
If John's scriptures are ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002",
        "02001003"], then
filterBible(scripture, "01", "001") => ["01001001","01001002"]

[input] array.string scripture

An array of the scriptures' ids, sorted by ASC.

[input] string book

Book id (2 letters)

[input] string chapter

Chapter id (3 letters)

[output] array.string

A filtered array with verses from the given chapter in the given book of the Bible."""
# test = ["01001003", "01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
# def filterBible(scripture, book, chapter):
#     lst = []
#     for scr in scripture:
#         if book+chapter == scr[:-3]:
#             lst.append(scr)
#
#     return sorted(lst)
#
# print(filterBible(test, '01', '001'))

# __________________________________________________________________________________________________
"""
Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string
that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)

[output] boolean
"""
# import itertools
# def isPalindrome(str):
#     for perm in itertools.permutations(str):
#         if perm == perm[::-1]:
#             return True
#     return False


# p = [3, 4, 1, 2, 5]
# q = [4, 5, 2, 3, 1]


# __________________________________________________________________________________________________

'''Convert a certain expression like 2+3 to expression in a postfix notation.

The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
division (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].

[execution time limit] 4 seconds (py)

[input] array.string expression

An array of tokes of a valid expression in the standard notation.

[output] array.string

Tokens of the expression in the postfix notation.
'''
# test0 = ['(','9','+','9',')','*','4','*','(','2', '+', '3',')']
# test = ['20', '+', '3', '*', '(', '5', '*', '4', ')'] # ['20', '3', '5', '4', '*', '*', '+']
# test1 = ['(', '(', '(', '1', '+', '2', ')', '*', '3', ')', '+', '6', ')', '/', '(', '2', '+', '3', ')']
# ['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']
# def toPostFixExpression(e):
#     op = '/+-*%'
#     length_e = len(e)
#     opend = 0
#     stack = []
#     result = []
#     for char in e:
#         if str(char).isdigit():
#             result.append(char)
#         elif char == '(':
#             opend += 1
#         elif char == ')':
#             opend -= 1
#             result.append(stack.pop())
#         elif char in op:
#             stack.append(char)
#     while stack:
#         result.append(stack.pop())
#
#     return result
#
# print(toPostFixExpression(test0))

# __________________________________________________________________________________________________

desc = [10, 5, 4, 6]
ascend = [3, 7, 10, 8]


'''Write a program that given an array of integers determines if it is sorted in "ascending" order, "descending" order or "not sorted" at all.

Example

For a = [10, 5, 4], the output should be
order(a) = "descending";
For a = [6, 20, 160, 420], the output should be
order(a) = "ascending";
For a = [1, 7, 0, 4, 8, 1], the output should be
order(a) = "not sorted".
[input] array.integer a

1 < a.length < 100, all of numbers are different

[output] string

"ascending", "descending" or "not sorted".'''
# def order(a):
#     for i in range(len(a)-1):
#         if a[i+1] > a[i]:
#             if i+2 == len(a):
#                 return 'ascending'
#             continue
#         else:
#             break
#
#     for i in range(len(a)-1, -1, -1):
#         if a[i] < a[i-1]:
#             if i == 1:
#                 return 'descending'
#             continue
#         else:
#             break
#
#     return 'unordered'
#
#
# print(order(desc))

''''s3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study as much before his current exams.

Example:

For a = [2,2,1,3,4,1] the answer is 3.

[input] array.integer a

The number of hours he studied each day.

[output] integer

The length of the maximum non-decreasing contiguous subarray.'''
a = [2, 2, 1, 3, 4, 1]
# def studying_hours(a):
#     lst_max = []
#     counter = 1
#     for i in range(len(a) - 1):
#         if a[i] <= a[i+1]:
#             counter+=1
#         else:
#             lst_max.append(counter)
#             counter = 1
#     lst_max.append(counter)
#
#     return max(lst_max)
#
# print(studying_hours([2,2,9]))


'''Nicky and Dev work in a company where each member is given his income in the form of points. On Nicky's birthday, Dev decided to give some of his points as a gift. The number of points Dev is gifting is the total number of visible zeros visible in the string representation of the N points he received this month.

Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0, Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.

Given the number of points N Dev received this month, calculate the number of points Nicky will receive as a gift and return this number in its binary form.

Note: visible zeros are calculated as follows:

0, 6 and 9 contain 1 visible zero each;
8 contains 2 visible zeros;
other digits do not contain visible zeros.
Example

For N = "565", the output should be
Cipher_Zeroes(N) = 10.

There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
210 = 102, so the output should be 10.

Input/Output

[input] string N

The number of points Dev received this month.

Constraints:
1 ≤ N ≤ 101000.

[output] integer

The number of points Nicky will receive in the binary representation.'''
# def Cipher_Zeroes(N):
#     zer_d = {1: ['0', '6', '9'], 2: ['8']}
#     counter = 0
#     for i in str(N):
#         if i in zer_d[1]:
#             counter += 1
#         elif i in zer_d[2]:
#             counter += 2
#     if counter % 2 == 0 and counter > 0:
#         counter -= 1
#     else:
#         counter += 1
#
#     print(counter)
#
#     b = ''
#     while counter > 0:
#         b = str(counter % 2) + b
#         counter //= 2
#     return b #if b != '1' else 0
#         # company gives one additional point
#
#
# print(Cipher_Zeroes('4'))
'''
Given two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].

Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

Example

Input:
p = [5, 1, 3],  q = [3, 1, 5]

Output:
r = [3, 2, 1]
[input] array.integer p

[input] array.integer q

[output] array.integer

permutation r
'''
# def findPermutation(p, q):
#     res = []
#     for n in q:
#         res.append(p.index(n) + 1)
#     return res

# q = [2, 1, 3]
# p = [3, 1, 2]
# print(findPermutation(p, q))


# p = [3, 4, 1, 2, 5]
# q = [4, 5, 2, 3, 1]
# [2, 5, 4, 1, 3]

# r - список індексів. Тобто якщо ми проходимо через q то елемент номер і в q буде також і в p, але під індексом r[i]
# Тому все що потрібно це for n in q
# І для кожного n треба знайти його індекс в списку p і записати його в r
# Але тут трошки дивна нумерація, тому в r треба записувати індекс+1


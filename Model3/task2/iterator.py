# my_list = [1, 2, 3, 4, 5, 6]

# iterator = iter(my_list)
# try:
#    print(next(iterator))
#    print(next(iterator))
#    print(next(iterator))
#    print(next(iterator))
#    print(next(iterator))
#   print(next(iterator))
# except (StopIteration, TypeError) as e:
#    print(e)


# print(my_list)

"""
Class Interator Example👇
"""
# class IteratorTest:
#     def __init__(self, limit=0):
#         self.limit = limit
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.limit:
#             number = 2 * self.n
#             self.n += 1
#             return number
#         else:
#             raise StopIteration
#
#
# num = IteratorTest(21)
# iterator1 = iter(num)
#
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
"""
List'dagi juft sonlarni chkarish👇
"""
# my_list = list(range(1, 21))
#
# iterator = iter(my_list)
#
# for iter1 in iterator:
#     if iter1 % 2 == 0:
#         print(iter1)

"""
Generator Iterable Example
"""
# def generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# my_generator = generator()
# try:
#     print(next(my_generator))
#     print(next(my_generator))
#     print(next(my_generator))
#     print(next(my_generator))
# except StopIteration as e:
#     print(e)

"""
yield bo'lsa Generator boladi!
"""

"""
Funkisiya Generatorsiz
"""
# def square(nums):
#     for num in nums:
#         return num
#
#
# numbers = list(range(1, 4))
# generator = square(numbers)
#
# print([number for number in numbers])
"""
Function for Generator
"""
# def square(nums):
#     for num in nums:
#         yield num
#
#
# numbers = list(range(1, 4))
# generator = square(numbers)
#
# print([number for number in numbers])

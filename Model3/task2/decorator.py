# def first_func(num):
#     """Second Function"""
#
#     def second_func(x):
#         return num * x
#
#     return second_func
#

def first_f(a):
    def second_f(b):
        return a / b

    return second_f


first = first_f(5)
second = first_f(5)

print(first(10))
print(second(10))

def even_filter(number):
    return number % 2 == 0


def only_even_parameters(func):
    def math_mult(*args):
        if len(args) == len([num for num in filter(even_filter, args)]):
            return args
        else:
            print('Please add only even numbers!')

    return math_mult


@only_even_parameters
def mult(a, b, c, d):
    return a * b * c * d


print(mult(6, 4, 2, 1))


@only_even_parameters
def add(a, b):
    return a + b


print(add(2, 4))

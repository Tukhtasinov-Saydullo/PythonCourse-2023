def only_even_parameters(func):
    def add_nums(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return a + b
        print("Please add only even numbers!")

    return add_nums


def only_even_parameters2(func):
    def math_mult(a, b, c, d):
        if a and b and c and d % 2 == 0:
            return a * b * c * d
        print('Please add only even numbers!')

    return math_mult

@only_even_parameters2
def mult(a, b, c, d):
    return a * b * c * d


@only_even_parameters
def add(a, b):
    return a + b


print(add(2, 2))

print(mult(6, 4, 2, 2))

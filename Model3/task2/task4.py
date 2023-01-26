def only_even_parameters(func):
    def add_nums(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return a + b
        else:
            print("Please add only even numbers!")

    return add_nums


@only_even_parameters
def add(a, b):
    return a + b


print(add(2, 1))

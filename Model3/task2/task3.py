def first_decorator(func):
    def del_2(a, b):
        return (a + b) * 2

    return del_2


@first_decorator
def second_dec(a, b):
    return (a + b) * 2


print(second_dec(2, 3))
print(second_dec(5, 5))

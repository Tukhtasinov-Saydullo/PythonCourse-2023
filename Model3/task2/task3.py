def first_decorator(func):
    def del_2(*args):
        return func(args) * 2

    return del_2


@first_decorator
def second_dec(*args):
    return sum(args)


print(second_dec(2, 3))
print(second_dec(5, 5))

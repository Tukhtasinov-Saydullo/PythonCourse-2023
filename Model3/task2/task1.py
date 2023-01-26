"""
Task 1
"""


def get_next_multiple(a: int):
    while True:
        yield a
        a = a * 2


gen_multiple_of_two = iter(get_next_multiple(2))
try:
    print(next(gen_multiple_of_two))
    print(next(gen_multiple_of_two))
    print(next(gen_multiple_of_two))
    print(next(gen_multiple_of_two))
except StopIteration as e:
    print(e)
gen_multiple_of_thirteen = get_next_multiple(13)
try:
    print(next(gen_multiple_of_thirteen))
    print(next(gen_multiple_of_thirteen))
    print(next(gen_multiple_of_thirteen))
    print(next(gen_multiple_of_thirteen))
except StopIteration as e:
    print(e)

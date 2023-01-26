def prime_numbers():
    for num in range(1, 1000):
        if all(num % i != 0 for i in range(2, num)):
            yield num


number = iter(prime_numbers())
try:
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
except StopIteration as e:
    print(e)

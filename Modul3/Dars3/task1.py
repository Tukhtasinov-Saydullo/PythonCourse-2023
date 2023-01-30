def range_one_to_twenty(n):
    _c_ = 1
    while _c_ < n:
        if _c_ % 2 == 0:
            yield f"-{_c_}"
        else:
            yield _c_
        _c_ += 1


for num in range_one_to_twenty(20):
    try:
        print(num)
    except StopIteration as e:
        print(e)

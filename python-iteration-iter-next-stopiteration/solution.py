def consume_iterator(iterable) -> list:
    """
    Obtain an iterator from `iterable` and manually consume it
    using `next()` until `StopIteration`.

    Return a new list containing all values in the original
    iteration order.

    Do not use a `for` loop.

    Example:
        consume_iterator([1, 2, 3]) -> [1, 2, 3]
        consume_iterator([]) -> []
    """
    a = []
    value = iter(iterable)
    while True:
        try:
            a.append(next(value))
        except StopIteration:
            break
    return a
            


def take_first(iterable, count: int) -> list:
    """
    Obtain an iterator from `iterable` and consume at most
    `count` values using `next()`.

    If the iterable becomes exhausted before `count` values are
    produced, stop early.

    If `count <= 0`, return an empty list.

    Example:
        take_first([10, 20, 30], 2) -> [10, 20]
        take_first([10], 5) -> [10]
    """
    a=[]
    value = iter(iterable)
    while (count>0):
            try:
                a.append(next(value))
                count= count-1
            except StopIteration:
                break
            
    return a


def next_or_default(iterator, default):
    """
    Call `next()` on the supplied iterator.

    Return the next value if one exists. If the iterator is
    exhausted, return `default`.

    Do not treat a produced value such as None, 0, or False as
    exhaustion.
    """
    while True:
        try:
            return next(iterator)
        except StopIteration:
            return default

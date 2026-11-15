def is_iterator(obj) -> bool:
    if iter(obj) is obj:
        return True
    else:
        return False


def get_iterator(iterable):
    return iter(iterable)
        


def independent_iterators(values: list) -> tuple:
    a1 = iter(values)
    a2 = iter(values)
    return (a1,a2)

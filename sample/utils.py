

def is_iterable(object) -> bool:
    try:
        iter(object)
    except TypeError:
        return False
    else:
        return True


def square(length : int):
    if not isinstance(length, int):
        raise TypeError
    for n in range(length):
        yield n ** 2
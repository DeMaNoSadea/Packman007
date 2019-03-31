def counter(func):
    func.__invocation_count__ = 0

    def wrapper(*args, **kwargs):
        func.__invocation_count__ += 1
        res = func(*args, **kwargs)
        print()
        print("{0} была вызвана: {1}x".format(func.__name__, func.__invocation_count__))
        print()
        return res
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args)
        return res
    return wrapper


@logging
@counter
def reverse_string(string):
    return str(reversed(string))


# Тут вместо последовательности выводился интератор

print(reverse_string('А роза упала на лапу Азора"'))
print(reverse_string('122221'))

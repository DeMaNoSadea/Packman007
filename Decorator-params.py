def appender(*args):
    def _doc(func):
        params = ''.join([defaultdocs[arg] for arg in args])
        func.__doc__ += '\n' + params
        return func
    return _doc


defaultdocs = {
    'a':
    """
    a : int, default 0
        the first parameter
    """,

    'b':
    """
    b : int, default 1
        the second parameter
    """
    }


@appender('a')
def f(a):
    return a


@appender('a', 'b')
def g(a, b):
    return a + b


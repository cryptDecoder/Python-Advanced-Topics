"""
A decorator takes in a function, adds some functionality and returns it.
"""


def smart_divide(func):
    def inner(a, b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            print("Whoops! Cant divide")
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(10, 4)


# Another on decorator
def star(fun):
    def inner(*args, **kwargs):
        print("*" * 30)
        fun(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(fun):
    def inner(*args, **kwargs):
        print("%" * 30)
        fun(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello, This is a decorator")

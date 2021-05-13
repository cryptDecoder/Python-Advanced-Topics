def sum(msg, *args):
    if msg:
        return sum(args)


print(sum("Hello", 22, 33))

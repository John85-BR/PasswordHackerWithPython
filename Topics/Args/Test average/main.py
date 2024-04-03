def average_mark(*args):
    total = 0

    for i in args:
        total += i

    return round(total / len(args), 1)



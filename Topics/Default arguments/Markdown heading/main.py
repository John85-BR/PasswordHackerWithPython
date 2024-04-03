def heading(string, num=1):
    if num <=0:
        num = 1

    if num > 6:
        num = 6

    return f"{num*'#'} {string}"

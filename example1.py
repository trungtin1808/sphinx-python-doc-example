def func1(arg1, arg2):
    """
    This function take two arguments, sets the first to equal the second, the return the new first argument. Pointless.

    :param arg1: Some value

    :param arg2: Another value

    :return: arg1

    """
    arg1 = arg2
    return arg1

def func2():
    """
    This function no arguments

    :return: None
    """
    return None

def func3(arg1, arg2):
    """
    This is a function with 2 arguments, return the result with the largest value of the 2 arguments

    :param arg1: with type integer
    :param arg2: with type integer

    :return: the largest value of the 2 arguments

    """
    if arg1 > arg2 : return arg1
    return arg2


def whyDontuseCamelCase(argument):
    return argument > 2


def reallyComplexFunction(arg1, arg2, arg3, arg4, arg5):
    """Fairly complicated function that returns arbitrary integer"""
    some_value = whyDontuseCamelCase(arg1)
    if some_value:
        return some_value
    if arg1:
        if arg2 and arg3:
            return 1
        elif arg2 and not arg3:
            return 2
        return 3
    elif arg4 and arg5:
        return 4
    return 5

# FIRST CLASS FUNCTIONS #############


def divide(divident, divisor):
    if divisor == 00:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return divident / divisor


def calculate(*values, operator):
    return operator(*values)

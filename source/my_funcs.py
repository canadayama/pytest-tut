def add(num1, num2):
    return num1 + num2


def divide(num1: int, num2: int) -> int:
    if num2 == 0:
        raise ValueError()
    return num1 / num2

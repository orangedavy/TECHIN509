def factorial(x):

    # recursive call until number reaches 1
    return 1 if x <= 1 else x * factorial(x - 1)


def inc(x: int) -> int:
    # Increments and returns the given integer
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x + 1


def dec(x: int) -> int:
    # Decrements and returns the given integer
    if not isinstance(x, int):
        raise TypeError("Given number is not an integer.")
    return x - 1


def add(x: int, y: int) -> int:
    # Adds and returns two given integers with increment and decrement functions
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Given input is not an integer.")
    if x < 0 or y < 0:
        raise ValueError("One or more inputs are less than 0.")

    # recursive call until second number becomes 0
    return add(inc(x), dec(y)) if y > 0 else x


def add_mod(x: int, y: int) -> int:
    # Adds and returns two given integers with increment and decrement functions
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Given input is not an integer.")

    if y < 0:
        # reverse dec and inc if y is negative
        return add_mod(dec(x), inc(y)) if y < 0 else x

    else:
        # remains the same
        return add_mod(inc(x), dec(y)) if y > 0 else x


def leap_year(x):

    # 'No' is easier to define with boolean values
    return 'No' if not x % 100 and x % 400 or x % 4 else 'Yes'


def fibonacci(n):

    if not isinstance(n, int) or n < 0:
        # input validation
        raise ValueError('Please change a number.')

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        # first two numbers
        return 1

    else:
        # recursive call of previous two numbers
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(factorial(10))
    print(leap_year(2400))
    print(fibonacci(14))
    print(add(9, 19))
    print(add_mod(9, 10))
    print(add_mod(-9, 10))
    print(add_mod(9, -10))
    print(add_mod(-9, -10))

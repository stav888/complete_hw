"""Recursive solutions for the 09.03.2026 homework."""


def print_down(n: int) -> None:
    if n <= 0:
        return
    print(n, end=" " if n > 1 else "")
    print_down(n - 1)


def sum_odd(n: int) -> int:
    if n <= 0:
        return 0
    return (n if n % 2 else 0) + sum_odd(n - 1)


def power(base: float, exponent: int) -> float:
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def max_in_list(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    if len(values) == 1:
        return values[0]
    return max(values[0], max_in_list(values[1:]))


def count_even(values: list[int]) -> int:
    if not values:
        return 0
    return int(values[0] % 2 == 0) + count_even(values[1:])


def sum_digits(number: int) -> int:
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


if __name__ == "__main__":
    print_down(5)
    print()
    print(sum_odd(7))
    print(power(2, 4))
    print(max_in_list([3, 8, 2, 15, 6]))
    print(count_even([2, 5, 8, 7, 6, 3, 10]))
    print(sum_digits(583))

# group of pre-defined functions
import math as m

number = 45

# 3.95 ~ 4
# print(math.fabs(number))


# count the number of digits
# 345
def count_digits(n: int) -> int | None:
    return round(m.log10(n) + 1)


# python function structure
# func(parameter: type) -> (return value type) | None:


print(count_digits((123)))

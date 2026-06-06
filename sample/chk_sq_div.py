# 4: 4 * 4 = 16
# 3: 3 * 3 = 9

# program: chk sq divisbility check even or odd
# Given a number, find it's square and check if the result is even or odd


def check_sq_div(n: int) -> bool | None:
    return pow(n, 2) % 2 == 0


print(check_sq_div(7))

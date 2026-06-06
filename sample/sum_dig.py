number = 14329087263623
# []
# 1 + 2 + 3 = 6
# 123 % 10 = 3 (res)
# 123 / 10 = 12 (again loop continues)


# def find_sum_of_digits(n: int) -> int | None:
#     res = 0
#     while n > 0:
#         res += n % 10
#         # print(res)
#         n //= 10  # 12 // 10 = 1
#     return res


# 123 = ['1', '2, '3']
conv_lst = list((str(number)))
# print(conv_lst)

# ['1', '2', '3'] -> sum([1, 2, 3])
# print([int(x) for x in str(number)])


def calculate_sum_dig(n: int) -> int | None:
    return sum([int(x) for x in str(n)])


# print(list(str(number)))

# print(sum(sorted([int(x) for x in str(number) if int(x) % 2 == 0])))

# '3' % 2 invalid
# 3 % 2 ✅

print(sum(sorted([int(x) for x in str(number) if int(x) % 2 == 0])))

# x % 2 == 0


def calculate_sum_even(n: int) -> int | None:
    return sum(sorted([int(x) for x in str(number) if int(x) % 2 == 0]))


# print(calculate_sum_even(14329087263623))

# print(find_sum_of_digits(1432))

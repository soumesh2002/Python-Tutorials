"""
*
* *
* * *
* * * *
"""

# for i in range(1, 5):
#     print(i * "* ")

"""
* * * *
* * * *
* * * *
* * * *
"""

# for i in range(5):
#     for j in range(5):
#         print("* ", end=" ")
#     print()

"""
* * * *
* * *
* *
*
"""

# for i in range(1, 5):
#     # range(1, 5): 1 to 4 `(1 to n - 1)`
#     for j in range(i, 5):
#         print("* ", end=" ")
#     print()

"""
1
1 2 
1 2 3
1 2 3 4

1
1 (1 + 1)
1 (1 + 1) (1 + 2)
1 (1 + 1) (1 + 2) (1 + 3)
"""
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

"""
1 2 3 4
1 2 3
1 2 
1
"""
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""
    *
  * * *
* * * * *

1 2 * 4 5
1 * * * 5
* * * * *

3 = 5 - 1 - 1 (space)
*: 2 * 1 + 1
"""

n = 5
for i in range(n):
    print(" " * (n - i - 1), end=" ")
    print("* " * (i + 1))

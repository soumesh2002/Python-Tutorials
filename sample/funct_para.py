# class Rectangle:
#     def __init__(self, length: float, breadth: float) -> None:
#         self.length = length
#         self.breadth = breadth

#     def calc_perimeter(self):
#         return 2 * (self.length + self.breadth)

#     def calc_area(self):
#         return self.length * self.breadth


# rect = Rectangle(45, 20)
# print(rect.calc_perimeter())


def calc_perimter(length: float, breadth: float) -> float | None:
    """
    Calculate the perimeter of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle.
    breadth : float
        The breadth (width) of the rectangle.

    Returns
    -------
    float
        The perimeter of the rectangle, computed as 2 * (length + breadth).
    None
        Returned if invalid input is provided.
    """
    return 2 * (length + breadth)


# **args, **kwargs


print(calc_perimter(32.987662, 14.3232))

# formatted strings
print(f"{calc_perimter(32.987662, 14.3232):.2f}")


def nMultiple(a=0, num=1):
    return a * num


print(nMultiple(num=6, a=5))

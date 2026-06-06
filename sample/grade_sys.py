"""
if else-if

dictionary
{'A': 95 - 100}

match (switch case alternatives)
"""


def grade_system(score: int) -> str:
    # Dictionary mapping grade boundaries
    grades = {
        "A": range(90, 101),
        "B": range(75, 90),
        "C": range(60, 75),
        "D": range(40, 60),
        "F": range(0, 40),
    }

    print(grades.items())

    # Loop through dictionary to find grade
    for grade, marks in grades.items():
        if score in marks:
            return grade
    return "Invalid Score"


# Test cases
print(grade_system(34))
print(grade_system(95))  # A
print(grade_system(82))  # B
print(grade_system(67))  # C
print(grade_system(45))  # D
print(grade_system(20))  # F

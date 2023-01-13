# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average


def calculate_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade < 90:
        return "B"
    elif grade >= 70 and grade < 80:
        return "C"
    elif grade >= 60 and grade < 70:
        return "D"
    return "F"

print(calculate_grade(85))
print(calculate_grade(55))
print(calculate_grade(72))
print(calculate_grade(95))
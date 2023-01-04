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

def calculate_grade(values):
    if values >= 90:
        return 'A'
    if values >= 80 and values < 90:
        return 'B'
    if values >= 70 and values < 80:
        return 'C'
    if values >= 60 and values < 70:
        return 'D'
    else:
        return 'F'

print(calculate_grade(91))

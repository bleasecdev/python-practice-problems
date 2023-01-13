# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

from statistics import mean


def calculate_average(numbers):
    if numbers == []:
        return None
    else:
        return mean(numbers)


print(calculate_average([1, 2, 3, 4]))
print(calculate_average([]))

# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    # Check if the list is empty or has only one element
    if values == [] or len(values) == 1:
        return None

    # Sort the list in descending order
    values.sort(reverse=True)

    # Return the second element in the sorted list
    return values[1]

print(find_second_largest([1,1,2,3,4]))
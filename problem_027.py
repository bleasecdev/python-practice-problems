# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if values == []:
        return None
    return max(values)

print(max_in_list([1,2,3]))
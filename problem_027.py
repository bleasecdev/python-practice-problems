# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(numbers):
    if numbers == []:
        return None 
    return max(numbers)

print(max_in_list([]))
print(max_in_list([1,2,3,4]))



# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(li):
    if len(li) % 2 == 0:
        return li[:(int(len(li)/2))], li[int(len(li)/2):]
    else:
        return li[:(int(len(li))-1)] , li[int(len(li))-1:]
    


print(halve_the_list([1,2,3,4]))
print(halve_the_list([1,2,3]))
print(halve_the_list([1,2,3,4,5,6,7]))
# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    num_in_mem_list = int(len(members_list))/2
    if int(len(attendees_list)) >= num_in_mem_list:
        return True
    return False


print(has_quorum(['a', 'b', 'c', 'd', 'e'], ['a','b','c','d','e','f','g','h','i','k','l']))
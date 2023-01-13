# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.


def has_quorum(num_of_attendees, num_of_members):
    if num_of_attendees >= num_of_members/2:
        return True
    return False

print(has_quorum(51, 100))
print(has_quorum(50, 115)) 



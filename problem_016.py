# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.



def is_inside_bounds(x, y):
    if x in range(0, 11) and y in range(0, 11):
        return True
    return False

print(is_inside_bounds(2,2))
print(is_inside_bounds(10,10))

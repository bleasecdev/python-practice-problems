# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
import random
def max_of_three(val1, val2, val3):
    if val1 >= val2 and val1 >= val3:
        return val1
    elif val2 >= val1 and val2>= val3:
        return val3
    return val3


print(max_of_three(1,6,1))
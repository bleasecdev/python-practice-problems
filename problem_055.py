# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"

def simple_roman(value):
    if value == 1:
        return "I"
    if value == 2:
        return "II"
    if value == 3:
        return "III"
    if value == 4:
        return "IV"
    if value == 5:
        return "V"
    if value == 6:
        return "VI"
    if value == "7":
        return "VII"
    if value == 8:
        return "VIII"
    if value == 9:
        return "IX"
    if value == 10:
        return "X"

print(simple_roman(10))

# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(sunny, workday):
    output = []

    if sunny == False and workday == True:
        output.append("umbrella")
    if workday == True:
        output.append("laptop")
    if workday == False:
        output.append("surfboard")
    return output        


print(gear_for_day(False, True))
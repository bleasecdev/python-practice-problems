# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    list = []
    if is_workday == True and is_sunny == False:
        list.append('Umbrella')
    if is_workday == True:
        list.append('Laptop')
    if is_workday == False:
        list.append('surfboard')
    return list

print(gear_for_day(is_workday= False, is_sunny=True))



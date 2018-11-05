""" Day2011 """
def calendar(day, month):
    """ day """
    days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return days[(day+months[month-1])%7]

print(calendar(int(input()), int(input())))

''' NumDays '''
from datetime import date
def day(day_1, month_1, day_2, month_2):
    ''' for '''
    try:
        return abs(date(2018, month_1, day_1)-date(2018, month_2, day_2)).days
    except ValueError:
        return 'Impossible'

print(day(int(input()), int(input()), int(input()), int(input())))

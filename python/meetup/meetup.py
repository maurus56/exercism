import calendar
from datetime import date

def meetup_day(year, month, day_of_the_week, which):
    days = {
        'Monday'    : 0, 'Tuesday'   : 1,'Wednesday' : 2,'Thursday'  : 3,
        'Friday'    : 4,'Saturday'  : 5,'Sunday'    : 6}

    index = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, 'last': -1}
    day_num = []
    weeks = calendar.monthcalendar(year,month)
    for week in weeks:
        if week[days[day_of_the_week]] != 0:
            day_num.append(week[days[day_of_the_week]])

    if which in index:
        day = day_num[index[which]]
    elif which == 'teenth':
        day = [d for d in day_num if 12 < d < 20][0]
    else:
        raise Exception()

    return date(year, month, day)

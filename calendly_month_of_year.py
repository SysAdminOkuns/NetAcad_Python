## https://python-programs.com/python-program-for-calendar-monthdayscalendar-method-with-examples/
## https://docs.python.org/3/library/calendar.html
from calendar import monthrange
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 and year > 1582:
        print("Leap Year!")
        return True
    elif year % 4 == 0 and year % 400 == 0 and year > 1582:
        print("leap Year!")
        return True
    elif year < 1582:
        print("Not within the gregorian calendar.")
        return False
    else:
        print("Not a leap year.")
        return False

def days_in_month(year, month):
    return monthrange(year,month)[1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

import calendar

dow_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def is_year_leap(year):
    pass
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    pass
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
    return dow_list[calendar.weekday(year, month, day)]
    

print(day_of_year(1984, 11, 18))
import calendar

year = int(input())
month = int(input())

days = calendar.monthrange(year, month)[1]

print(days)

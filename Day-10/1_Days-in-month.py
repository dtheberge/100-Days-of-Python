def is_leap(year):
    ans = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                ans = True
            else:
                ans = False
        else:
            ans = True
    else:
        ans = False

    return ans


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not is_leap(year) or not month == 2:
        return month_days[month - 1]
    return 29


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

day=int(input("day"))
month=int(input("month"))
year=int(input("year"))


if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2022:
    year=year%100
    if day<1 or day>31:
        print("invalid date")
    else:
       if month<1 or month>12:
        print("invalid date")
       else:
           print(f"you date is: {day}/{month}/{year}")

    if 1<=day<=9 or 1<=month<=9:
        year=year%100
        month=str(month)
        month="0"+month
        day=str(day)
        day="0"+day
        print(f"you date is: {day}/{month}/{year}")








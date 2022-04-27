

year = int(input("Enter year: "))

if year % 4 != 0 and year > 1582:
    if year % 400 != 0:
        print("Common year!")
elif year % 100 != 0 and year > 1582:
    print("Leap Year!")
elif year <= 1582:
    print("Not within the Gregorian Calendar period.")
else:
    print("Leap year!")
    


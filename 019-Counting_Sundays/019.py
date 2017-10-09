#Go from 1 Jan 1900 to 1 Jan 1901
day = 365 % 7
sundays = 0

#Loop through every year
for year in range(1901,2001):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #If it's a leap year
    if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
        months[1] = 29

    #Check if the beginning of the month is a sunday
    for month in months:
        if day == 6:
            sundays += 1

        day = (day + month) % 7

print(sundays)

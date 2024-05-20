# Write a program that takes a date as input and outputs the date's season
# The input is a string to represent the month and an int to represent the day.


# Input
month = input()
day = int(input())

# If input is other than valid months
if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December'):
    print('Invalid')
    exit()

if day < 1 or day > 31:
    print('Invalid')
    exit()

# Determine the maximum day for the given month
if month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
    max_day = 31
elif month == 'February':
    max_day = 29  # Assuming leap years
else:
    max_day = 30

# Determine the seasons based on month and day
if (month == 'March' and day >= 20) or (month == 'April') or (month == 'May') or (month == 'June' and day <= 20):
    season = 'Spring'
elif (month == 'June' and day >= 21) or (month == 'July') or (month == 'August') or (month == 'September' and day <= 21):
    season = 'Summer'
elif (month == 'September' and day >= 22) or (month == 'October') or (month == 'November') or (month == 'December' and day <= 20):
    season = 'Autumn'
else:
    season = 'Winter'

print(season)




def LeapYear_00():
    print('I can work out if a specific year is a Leap Year!')
    year = int(input('Enter the year?\n'))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year.')
            else:
                print(f'{year} is NOT a leap year.')
        else:
            print(f'{year} is a leap year.')
    else:
        print(f'{year} is NOT a leap year.')

LeapYear_00()
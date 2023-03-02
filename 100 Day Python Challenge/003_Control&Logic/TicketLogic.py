def TicketLogic_00():
    print('\nWelcome to the Travelling Circus, The home of thrills... NOT for Widows & Orphans!\n')
    height = int(input('What is your height in cm:\n'))
    if height >= 120:
        print('\nYour tall enough to ride :)\n')
        age = int(input('How old are you?\n'))
        if age <= 12:
            print('You pay $4.99 for a Day Pass')
        elif age < 18: # elif age > 12 and age < 18: # Not as efficient but show how to use 'and' in and if statement
            print('You pay $6.99 for a Day Pass')
        elif age >= 18:
            print('You pay $11.99 for a Day Pass')
    else:

        print('You do not meet the minimum height required to access our Rides!')

# TicketLogic_00()

def TicketLogic_01():
    print('\nWelcome to the Travelling Circus, The home of thrills... NOT for Widows & Orphans!\n')
    height = int(input('What is your height in cm:\n'))
    bill = float(0.00)
    # Check Height
    if height >= 120:
        print('\nYour tall enough to ride :)\n')
        age = int(input('How old are you?\n'))
        # Check Age
        if age <= 12:
            print('Child Ticket: You pay $4.99 for a Day Pass')
            bill = (bill + 4.99)
        elif age < 18: # elif age > 12 and age < 18: # Not as efficient but show how to use 'and' in and if statement
            print('Youth Ticket: You pay $6.99 for a Day Pass')
            bill = (bill + 6.99)
        elif age >= 18:
            print('Adult Ticket: You pay $11.99 for a Day Pass')
            bill = (bill + 11.99)
        # Up Sell
        photo = input('\nDo you want to capture your memories? With Photos of you on the rides.\nThis services is $9.99 for two photos, Add this to your ticket: Yes/No?\n')
        if photo == 'Yes':
            bill = (bill + 9.99)
            print(f'Day Pass + Photos = {bill}')
        elif photo == 'yes':
            bill = (bill + 9.99)
            print(f'Day Pass + Photos = {bill}')
        elif photo == 'Y':
            bill = (bill + 9.99)
            print(f'Day Pass + Photos = {bill}')
        elif photo == 'y':
            bill = (bill + 9.99)
            print(f'Day Pass + Photos = {bill}')
        # Up Sell = FAILED
        else:
            print(f'Day Pass = {bill}')
    # Not Tall Enough to RIDE!
    else:
        print('You do not meet the minimum height required to access our Rides!')

TicketLogic_01()
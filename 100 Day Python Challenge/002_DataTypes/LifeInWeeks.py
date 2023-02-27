def NumberOfWeeks():
    '''Number of Weeks Calculator'''
    # Ask Q1
    question_age = f'What is your current age? in years: \n'
    answer_age = int(input(question_age))
    # Calculate Age in Weeks
    seconds = int((60*(60*(24*365)))*answer_age)
    minutes = int((60*(24*365))*answer_age)
    hours = int((24*365)*answer_age)
    days = int(365*answer_age)
    weeks = int(52*answer_age)
    months = int(12*answer_age)
    quarters = int(4*answer_age)
    years = int(answer_age)
    # Return Years Left from average age of Death
    remainder = int(80 - answer_age)
    remainder_days = remainder * 365
    remainder_weeks = remainder * 52
    remainder_months = remainder * 12
    remainder_quarters = remainder * 4

    print(f'Your Age in; Seconds: {seconds}, Minutes: {minutes}, Hours: {hours}, Days: {days}, Weeks: {weeks}, Months: {months}, Quarters: {quarters}, Years: {years}\nWith a Remainder of: {remainder_days} Days, {remainder_weeks} Weeks, {remainder_months} Months, {remainder_quarters} Quarters, {remainder} Years, Assuming your the Mean Average of the Distribution of Age of Death.')

NumberOfWeeks()
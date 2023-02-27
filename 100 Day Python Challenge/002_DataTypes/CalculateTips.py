def TipCalculator():
    '''Calculates $ Tips which should be given to a Waiter'''
    # Ask Q1
    question_01 = f'\nHow Much is the total of your bill? \n'
    answer_01 = float(input(question_01))
    # Ask Q2
    question_02 = f'\nWhat % Percentage would you like to Tip? \n'
    answer_02 = float(input(question_02))

    tip = answer_01*(answer_02/100)
    total = float(answer_01+tip)
    print(f'\nYou should Tip the Staff: $ {tip:.2f} \nThis would bring your total to: $ {total:.2f} up from $ {answer_01:.2f} Ex-Tip of {answer_02:.2f}%\n')
    # Ask Q3
    question_03 = f'How many people intend to split the bill? \n'
    answer_03 = float(input(question_03))
    share = float(total/answer_03)
    print(f'\nTip the Staff: $ {tip:.2f} \nYour Total Spend: $ {total:.2f} \nEach Person Contributes: $ {share:.2f}\n')

TipCalculator()
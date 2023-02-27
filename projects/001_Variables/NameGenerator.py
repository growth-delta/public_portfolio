def NameGenerator(question1='Where is your Town/City of birth?', question2='What is your favoured word?',):
    '''Generates a name based on two input() question variables'''
    # Welcome Message
    welcome = '\nPlease answer the following questions to generate a name.\n'
    print(welcome)

    # Ask Q1
    question1 = f'\n{question1}\n'
    answer1 = input(question1)

    # Ask Q2
    question2 = f'\n{question2}\n'
    answer2 = input(question2)

    # Concat Answers
    print(f'\nThe name could be: {answer1} {answer2}')

NameGenerator()
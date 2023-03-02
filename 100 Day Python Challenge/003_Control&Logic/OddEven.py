def OddEven():
    '''
        This line of code checks whether an integer number is even or odd. Here's what it means at a high level:

        The % operator returns the remainder of the division of number by 2.
        If the remainder is 0, that means number is divisible by 2 and therefore even.
        If the remainder is 1, that means number is not divisible by 2 and therefore odd.

        So, the condition if number % 2 == 0 checks whether the remainder of number divided by 2 is 0, which indicates that number is even. 
        If the condition is true, the code inside the if block is executed, otherwise, the code inside the else block is executed.
    '''
    print('I will tell you if any whole number is odd or even!')
    number = int(input('\nWhat is the number you want to check?\n'))
    if number % 2 == 0:
        print(f'The number {number} is Even.')
    else:
        print(f'The number {number} is Odd.')

OddEven()
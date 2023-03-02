def BMIcalculator():
    '''BMI Calculator| Takes Weight kg and Height m as arguments to calculate a person Body Mass Index'''
    # Ask Q1
    question_height = f'What is your height? in Metres: \n'
    answer_height = float(input(question_height))
    # Ask Q2
    question_weight = f'What is your weight? in Kilograms: \n'
    answer_weight = float(input(question_weight))
    # Calculate BMI
    BMI = round(answer_weight / (answer_height ** 2))
    # Return BMI to Console in 2dp
    print(f'\nYour BMI is: {BMI:.2f}')
    if BMI < 18.5:
        print('You are Under Weight, according to the BMI metric.\n')
    elif BMI < 25:
        print('You are a Normal Weight, according to the BMI metric.\n')
    elif BMI < 30:
        print('You are Over Weight, according to the BMI metric.\n')
    elif BMI < 35:
        print('You are Obese, according to the BMI metric.\n"HA! HA!" -Nelson from the Simpsons\n')
    else:
        print('You are Clinically Obese, according to the BMI metric.\n"HA! HA!" -Nelson from the Simpsons\n')

BMIcalculator()
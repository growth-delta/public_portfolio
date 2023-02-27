def BMIcalculator():
    '''BMI Calculator| Takes Weight kg and Height m as arguments to calculate a person Body Mass Index'''
    # Ask Q1
    question_height = f'What is your height? in Metres: \n'
    answer_height = float(input(question_height))
    # Ask Q2
    question_weight = f'What is your weight? in Kilograms: \n'
    answer_weight = float(input(question_weight))
    # Calculate BMI
    BMI = answer_weight / (answer_height ** 2)
    # Return BMI to Console in 2dp
    print(f'Your BMI is: {BMI:.2f}')

BMIcalculator()
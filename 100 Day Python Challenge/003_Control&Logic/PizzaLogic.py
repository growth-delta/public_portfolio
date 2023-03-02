def PizzaOrder(capacity='Within the next Hour'):
    print("Welcome to De'Tomato Pizzeria. Place an Order NOW.")
    class Pricing:
        bill = float(0.00)
        small = float(4.99)
        medium = float(6.99)
        large = float(8.99)
        meat = float(2.99)
        cheese = float(1.99)
    bill = Pricing.bill

    while True:
        size = input('What size pizza are you making? S, M, L\n')
        if size in ['S', 's', 'small', 'SMALL', 'Small']:
            bill += Pricing.small
            break
        elif size in ['M', 'm', 'MEDIUM', 'Medium']:
            bill += Pricing.medium
            break
        elif size in ['L', 'l', 'LARGE', 'Large']:
            bill += Pricing.large
            break
        else:
            print("Invalid input. Please enter either 'S', 'M', or 'L'.")
    
    while True:
        topping1 = input(f'Thats ${bill}\n\nWould you like to add Specially Selected Italian Cured Meats to your pizza? for an extra ${Pricing.meat}\n')
        if topping1 in ['Yes', 'yes', 'YES', 'y', 'Y']:
            bill += Pricing.meat
            print(f'Thats ${bill}\n')
            break
        elif topping1 in ['No', 'no', 'NO', 'n', 'N']:
            break
        else:
            print("Invalid input. Please enter either 'Yes' or 'No'.")
    
    while True:
        topping2 = input(f'Your Bill = ${bill}\n\nWould you like to add Specially Selected Italian Mixed Cheese to your pizza? for an extra ${Pricing.cheese}\n')
        if topping2 in ['Yes', 'yes', 'YES', 'y', 'Y']:
            bill += Pricing.cheese
            print(f'Thats ${bill}\n')
            break
        elif topping2 in ['No', 'no', 'NO', 'n', 'N']:
            break
        else:
            print("Invalid input. Please enter either 'Yes' or 'No'.")
    
    while True:
        zip = input(f'\nBill = ${bill}\nProvide your ZIP code for delivery.\n')
        if zip.startswith(("BL", "bl")):
            print(f'\nDelivery: {capacity}\n')
            break
        else:
            print("Invalid input. Please enter a Valid Zip Code.")

PizzaOrder()
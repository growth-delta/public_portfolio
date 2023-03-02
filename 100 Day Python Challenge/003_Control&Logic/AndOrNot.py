def AndOrNot(random_variable=22):
    random_variable = int(input(f'Pick a Random Number Between 2 & 99:\n\n'))
    if random_variable >1 and random_variable <100:
        print(f'Its bigger than 1, but less 100... {random_variable}')
    if random_variable >=100 or random_variable <=1:
        print(f'You Scammer! It doesnt matter ill guess anyway {random_variable}')
    if not random_variable < 99:
        print(f'Trying to FAMOOSE me? It doesnt matter I will guess anyway {random_variable}')

AndOrNot()
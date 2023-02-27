fill_text = '------------------------'
# {} in an f'string' allows you to add extra data to the string
# \n Creates a enter/return (NEW LINE) in a string
alter_ego = f'The Port Maria Buccaneer\n{fill_text}\nThe Saint Mary Prirate'
# print('zyx') prints the output of python to the console
print(alter_ego)

# input('xyz question?') function allows users to 'input' data back into the pyhton console, when prompted
name = input("What is your name? ")
length = len(name)
print(f'Then {name} be your name, {name}! Dilly dilly!\n\nInteresting thats: {length} characters long.')

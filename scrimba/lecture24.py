
def greeting(name, age=28, color = 'red'):
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ') 
age = input('Enter your age: ')
color = input('Enter favorite color: ')
greeting(name, int(age), color)



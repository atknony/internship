a = int(input("Enter 1 for calculator, or enter 2 for convertor: "))

if a == 1:
    print("---calculator---")
    v1 = int(input("Enter first value: "))
    v2 = int(input("Enter second value: "))
    operator = input("Enter the number of operator 1:+, 2:-, 3:/, 4:* : ")
    if operator == "1":
        calc = v1 + v2
        print(f"calculation is {calc}.")
    if operator == "2":
        calc = v1 - v2
        print(f"calculation is {calc}.")
    if operator == "3":
        calc = v1 / v2
        print(f"calculation is {calc}.")
    if operator == "4":
        calc = v1 * v2
        print(f"calculation is {calc}.")
else:
    print("---conventer---")
    celcius = int(input("Enter a value: "))
    fahrenheit = celcius*9/5 + 32
    print(f"{celcius} C is {fahrenheit} F.")             








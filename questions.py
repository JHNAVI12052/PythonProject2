# pi = 3.24
# r = float(input("Enter the length: "))
# shape = input("Enter the shape: circle/square/triangle  ").lower()
# if shape == "circle":
#     area = pi * r**2
#     print(f"area of a circle is {area}")
# elif shape == "square":
#     area = r**2
#     print(f"area of a square is {area}")
# elif shape == "triangle":
#     area = 0.5*r*r
#     print(f"area of a triangle is {area}")
# else:
#     print("Invalid input")

#convert celius in fahrenheit and kelvin
# x = float(input("Enter the temperature in Celsius: "))
#
# F = x * 1.8 + 32
# K = x + 273.15
# print(f"The temperature in Fahrenheit is: {F}, The temperature in Kelvin is: {K}")

#simple calculator
num1= float(input("Enter the number of decimal places you want in the calculation: "))
num2 = float(input("Enter the number of decimal places you want in the calculation: "))
operation = input("Enter the operation you want to perform: addition/subtraction/multiplication/division: ").lower()
if operation == "addition":
    print(f"The result is: {num1 + num2}")
elif operation == "subtraction":
    print(f"The result is: {num1 - num2}")
elif operation == "multiplication":
    print(f"The result is: {num1 * num2}")
elif operation == "division":
    print(f"The result is: {num1 / num2}")
else:
    print("Invalid operation")




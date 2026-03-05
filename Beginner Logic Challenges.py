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
# num1= float(input("Enter the number of decimal places you want in the calculation: "))
# num2 = float(input("Enter the number of decimal places you want in the calculation: "))
# operation = input("Enter the operation you want to perform: addition/subtraction/multiplication/division: ").lower()
# if operation == "addition":
#     print(f"The result is: {num1 + num2}")
# elif operation == "subtraction":
#     print(f"The result is: {num1 - num2}")
# elif operation == "multiplication":
#     print(f"The result is: {num1 * num2}")
# elif operation == "division":
#     print(f"The result is: {num1 / num2}")
# else:
#     print("Invalid operation")

#EVEN ODD CHECKER
# even_or_odd = float(input("Enter the number: "))
# if even_or_odd % 2 == 0:
#     print("Even")
# elif even_or_odd % 2 != 0:
#     print("Odd")
# else:
#     print("invalid")

#GRADE CALCULATOR
# grade = float(input("What is your marks? "))
# if grade >= 90:
#     print("Grade = A+ 'outstanding")
# if grade >= 80:
#     print("Grade = A 'excellent")
# if grade >= 70:
#     print("Grade = B 'good'")
# if grade >= 60:
#     print("Grade = C 'average'")
# if grade >= 50:
#     print("Grade = P 'pass'")
# if grade <= 40:
#     print("Grade = F 'fail'")
# else:
#     print("Grade = N/A")

#DISCOUNT CALCULATOR
# price = float(input("What is your price? "))
# discount = float(input("What is the  discount? "))
# final_discount = discount/100*price
# final_price = price - final_discount
#
# print("Your final price is:", final_price)


#vowels counter
# word = input("Enter a word: ").lower()
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for char in word:
#     if char in vowels:
#         count += 1
#
# print('the no. of vowels present:',count)



#muliplication table
# multiple = int(input("table no of: "))
#
# for i in range(1, 11):
#     print(f"{multiple} * {i} = {multiple * i}")

#reverse a string
# string = input("Enter a word: ")
# reverse = string [::-1]

# print(reverse)

#simple interest calculator
# amount = float(input("How much money do you want to invest ?: "))
# time_period = int(input("How many years do you want to invest ?: "))
# rate = float(input("what is the rate ?: "))
# SI = amount*rate*time_period/100
# print(SI)

#password checker
# passcode = (input("Enter passcode: "))
# passcode.isdigit()
# if len(passcode) <= 6:
#     print("Your password is too weak")
# elif passcode.isalpha() or passcode.isdigit():
#
#     print("Your password is too medium, add some special characters")
# elif not any(ch in "!@#$%^&*()-_+=<>?/" for ch in passcode):
#     print("Your password is too strong")
# else:
#     print("Your password is too hard")

#guess the number game











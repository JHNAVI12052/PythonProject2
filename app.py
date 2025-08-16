

# course = 'python for beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.capitalize())
# print(course.title())
# print(course.find('p'))
# print(course.replace('beginners', 'absolute beginners'))
# print('python' in course)
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = price * 0.1
# else:
#     down_payment = price * 0.2
# # print(f"Down payment: ${down_payment}")
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# print("done")

# password input from user and match with original password else return input password again
# i = "admin123#"
# password = input("Enter password: ")
#
# while password != i:
#     print("Incorrect password. Try again.")
#     password = input("Enter password: ")
#
# print("Access Granted")

# i = 1
# total = 0
# while i <= 50:
#     if i % 2 == 0:
#       total += i
#     i += 1
# print("Sum of even digits:  ", total)

# # keep accepting words from user until they type exit
# while True:
#     word = input("Enter a word: ")
#     if word == "exit":
#         break
#     else:
#         print("you typed : ", word)
def isPalindrome(x):
    # Step 1: Handle negatives first
    if x < 0:
        print("Negative number. Cannot be a palindrome.")
        return False

    x_copy = x
    rev = 0

    print("\nDry Run Steps:")
    print("-" * 40)

    while x_copy != 0:
        digit = x_copy % 10
        x_copy = x_copy // 10
        rev = rev * 10 + digit

        print(f"digit: {digit}, x_copy now: {x_copy}, rev so far: {rev}")

    print("-" * 40)
    print(f"Original number: {x}, Reversed number: {rev}")

    return rev == x

# Run test
num = int(input("Enter a number: "))
if isPalindrome(num):
    print("✅ It is a Palindrome.")
else:
    print("❌ Not a Palindrome.")







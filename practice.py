# #find the largest of two numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# def find_largest(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print("the largest no. is : ", find_largest(a, b))
from contourpy.types import offset_dtype


# fizzBuzz
# num = int(input("Enter a number: "))
#
# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return num
#
# print(fizz_buzz(num))

#sum of digit
# def sum_of_digits(n):
#     total = 0
#     for digit in str(n):
#         total += int(digit)
#     return total

# count vowels in a string
# def find_min_max(nums):
#     min_num = min(nums)
#     max_num = max(nums)
#     return {"min": min(nums), "max": max(nums)}
# num = [4,10,3,2,8,6]
# print(find_min_max(num))

# def even_numbers(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# print(even_numbers(5))

# x = int(input("Enter a number: "))
# x_copy = abs(x)
# ans = 0
#
# print("\nDry Run Steps:")
# print("-" * 40)
#
# while x_copy != 0:
#     digit = x_copy % 10
#     x_copy = x_copy // 10
#     ans = ans * 10 + digit
#
#     print(f"digit: {digit}, x_copy now: {x_copy}, ans so far: {ans}")
#
# # Restore sign
# if x < 0:
#     ans = -ans
#
# print("-" * 40)
# print(f"After applying sign: {ans}")
#
# # Check 32-bit range
# if ans < -2**31 or ans > 2**31 - 1:
#     print("Out of 32-bit range. Returning 0.")
#     print(0)
# else:
#     print("Reversed number is:", ans)
# def is_even(n):
#     if n%2 ==0:
#         return 'even'
#     else:
#         return 'odd'
# n = int(input("type the number:  "))
# print(is_even(n))

#sum of digits

#         total = 0
#         while num >0:
#             total += num % 10
#             num = num // 10
#         num = total
#     return num
# print(sum_of_digits(29))
#list of squares of numbers from 0 to 4 using range
#
#shallow copy : create a new list object, so this would then modify only new opbect will not affect the original copy
#will create new copy of the outert list but will not crfaete the new copy of the inner list and will link them to the original copy so changing anything inside inner list would afftect the original ones also


#deep copy - we need to import copy module in python
#import copy
#list = [["x0", 1],["x2",2]]
#list_copy = copy.deepcopy(list)

#to summarise
#lista = listb -> refernce not copy
#lista = listb[:] ->shallow copy
#lista = list(listb) -> shallow copy
#lista = listb.copy() ->shallow copy


#slicing
#picking some spefic part of your list
#-> indexing : picking a element from a list by passing index
# my_list = ["alice","bob","charlie", "danile","jack"];
#
# print(my_list[1:-1])

#->get a sublist using slicing
#my_list[start_index:end_index]
#i give ntg in start index , it takes value as 0
#end index is empty , then teh default value is end of list
#

#-> get a list by using step
#list[start::end_step]
#end _step tells the code how many times it need to skip teh item . for eg if step is 3 take every third item
# my_list =[1,2,3,4,5,6,7,8,9,10]
# print(my_list[::3])
# print(my_list[2::3])

#WAP to reverse the list using slicing
# my_list = [1,2,3,4,5,6,7,8,9]
#
# print(my_list[::-1])
#WAP to filter even numbers from list
# my_list = [1,2,3,4,5,6,7,8,9]
# even_no =[n for n in my_list if n % 2 == 0]
#
# print(even_no)
#WAP to split list in two halves and print them
# my_list = [1,2,3,4,5,6,7,8,9]
# mid = len(my_list)//2
# first_half = my_list[:mid]
# second_half = my_list[mid:]
# print(first_half)
# print(second_half)

#WAP to remove duplicate from the list
# my_list = [1,2,3,4,5,6,7,8,8,8,9,1,3,4]
# my_list = list(set(my_list))
# print(my_list)

#wap sum every element in list
# my_list = [1,2,3,4,5,6,7,8,9]
# total = 0
# for i in my_list:
#     total += i
# print(total)
#  or
# sum= 0
# index = 0
# while index < len(my_list):
#     sum += my_list[index]
#     index += 1
# print(sum)

#find maximum element in a list
# my_list = [1,2,3,4,5,6,7,8,9,10]
# max_no = my_list[0]
#
# for i in my_list:
#     if i > max_no:
#         max_no = i
# print(max_no)
# find the sum of max and min element of an array (+ve integers)
# min_no = my_list[0]
# for i in my_list:
#     if i > max_no:
#         max_no = i
#     if i < min_no:
#         min_no = i
# sum_max_min = max_no + min_no
# print(sum_max_min)

## find out all the unique items of a list



# my_list=[1,2,3,3,3,2,1,2,4]
# unique_list = []
# for i in my_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# my_list = list(set(my_list))
# print(my_list)

#reverse a list
# my_list = [1,2,3,4,5,6,7,8,9]
# reverse_no = my_list[::-1]
# print (reverse_no)

#average of the list
# my_list = [1,2,3,4,5,6,7,8,9]
# total = 0
# for i in my_list:
#     total += i
# print("sum",total)
#
# avg = total / len(my_list)
# print("average",avg)
#WAP to revere an array or list.
# def reverse_list(nums):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
#     return nums
# print(reverse_list([1,2,3,4,5]))





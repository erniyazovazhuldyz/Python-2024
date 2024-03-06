nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_doubled = list(map(lambda x : x *2, nums))
print(nums_doubled)
#task1


def count_upper_lower(input_string):
    upper_count = sum(chr.isupper() for chr in input_string)
    lower_count = sum(chr.islower() for chr in input_string)
    print("number of upper case letters:", upper_count)
    print("number of lower case letters:", lower_count)

my_input = input("enter a string: ")
count_upper_lower(my_input)
#task2


def Is_palindrome(input_string):
    reversed_string = "".join(reversed(input_string))
    if reversed_string == input_string:
        print("This string is a palindrome")
    else:
        print("This string is not a palindrome")

my_input = input("enter a string: ")
Is_palindrome(my_input)
#task3


import time
import math
input_number = 25100
delay_milliseconds = 2123
time.sleep(delay_milliseconds / 1000)
result = math.sqrt(input_number)
print(f"Square root of {input_number} after {delay_milliseconds} milliseconds is {result}")
#task4



tuple = [1, True, 'hi', 3.14]
print("tuple, all, any:", all(tuple), any(tuple))
#task5









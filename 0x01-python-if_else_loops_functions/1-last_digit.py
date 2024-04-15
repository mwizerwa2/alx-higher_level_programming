#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number= int(input("Enter any five-digit number "))
last_digit= number % 10

if last_digit >5:
    comparison= 'and is greater than 5'

elif last_digit==0:
    comparison= 'and is 0'

elif 6> last_digit !=0:
    comparison= 'and is less than 6 and not 0'

else:
    "Please check the number"

print(f"Last digit of {number} is {last_digit} {comparison}")

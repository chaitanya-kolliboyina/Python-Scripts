# Exercise 1: Run the program on your system and see what numbers
# you get. Run the program more than once and see what numbers you
# get.

# import random

# for i in range(10):
#     print(random.random())

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (hours and rate).

def compute_pay(time:int, rate: int)->float:
    try:
        if time <= 40:
            sal = rate * time
        else:
            sal =  rate * 1.5 * (time-40) + rate * 40
    except:
        print("Please enter numeric output")
    return sal

time = int(input("Enter  hours worked: "))
per_hour = int(input("Enter rate: "))
print("pay : "+ str(compute_pay(time, per_hour)))
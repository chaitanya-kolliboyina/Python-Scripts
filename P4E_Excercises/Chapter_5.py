# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
# count = 0
# total = 0
# while True:
#     try:
#         num = input("Enter a number : ")
#         if num == 'done':
#             break
#         else:
#             count = count+1
#             total = total + int(num)

       
#     except:
#         count = count-1
#         print("Invalid data")
# print(total,count,total/count)

#Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

ls = []
while True:
    try:
        num = input("Enter a number : ")
        if num == 'done':
            break
        else:
            ls.append(int(num))

       
    except:
        
        print("Invalid data")
print(max(ls),min(ls))
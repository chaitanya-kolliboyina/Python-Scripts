### Prob 1: Check a number is eve or odd

# n = int(input("Enter n: "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

### Prob 2: Check a number is prime or  not 

# n = int(input("Enter n: "))
# flag = 1        ### default is set to prime
# if n<=1:
#     print("Not Prime")

# else:
#     for i in range(2,n):
#         if n%i==0:
#             flag = 0
#             print("Not Prime")
#             break
#     else:
#         flag = 1
#         print("Prime")

### Prob 3: Print factorial of Number 
# from timeit import default_timer as timer 

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#        fact = fact*i
#     return fact
    
# start = timer()
# n = int(input("Enter n: "))
# print(factorial(n))
# end = timer()
# print("Time elapsed : ", end-start)
##### Reverse of a number

# n = input()
# print(n[::-1])

##### Check palindrome

# n = input("Enter input : ")
# def check_palindrome(n:str )->bool :
#     rev = n[::-1]
#     if n == rev :
#         return True
#     else :
#         return False
# print(check_palindrome(n))

##### Check Prime number 

# n = int(input("Enter input : "))
# def check_prime(n: int) ->bool :

#     for i in range(2,n//2):
#         if n%i == 0 :
#             return False                           # IF n is checked untill square root of n, time complecity reduces to sqrt(n) - Optimal solution
#     else :
#         return True
           
# print(check_prime(n))
            
#### Print divisors of given number 
# from math import sqrt
# n = int(input("Enter input : "))                                     
# def print_divisors(n:int):
     
#     # for i in range(1,n+1):                                                 # Brute force TC :  O(n)
#     #     if (n % i == 0):
#     #         print(i)
    
#     for i in range(1,int(sqrt(n))+1):                                               # optimal force TC : O(sqrt(n))
#         if n % i == 0:
#             print(i,end = " ")

#         if i != n/i :
#             print(int(n/i),end = " ") 
# print(print_divisors(n))

 
#### ARmstrong number 

# num = input("Enter number : ")
# exp = len(num)
# original = int(num)
# num = int(num)
# sun = 0
# while num > 0 :
#     s = num % 10
#     sun = sun + s ** exp 
#     num = num // 10

# if sun == original :
#     print("Yes")
# else :
#     print("No")

#### GCD 

a,b = input().split()
ans = []                                        # Brute force TC : O(n)
a = int(a)
b = int(b)
for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i ==0 :
        ans.append(i)
print(ans)
print(max(ans))




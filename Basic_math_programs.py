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

n = int(input("Enter input : "))
def print_divisors(n:int) ->list:
    ls = [] 
    for i in range(1,n+1):
        if (n%i == 0):
            ls.append(i)
    return ls

print(print_divisors(n))






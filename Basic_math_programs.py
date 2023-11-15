# Reverse of a number

# n = input()
# print(n[::-1])

#Check palindrome

# n = input("Enter input : ")
# def check_palindrome(n:str )->bool :
#     rev = n[::-1]
#     if n == rev :
#         return True
#     else :
#         return False
# print(check_palindrome(n))

# Check Prime number 

n = int(input("Enter input : "))
def check_prime(n: int) ->bool :

    for i in range(2,n//2):
        if n%i == 0 :
            return False
    else :
        return True
        
    
print(check_prime(n))
            





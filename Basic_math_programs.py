# Reverse of a number

# n = input()
# print(n[::-1])

#Check palindrome

n = input("Enter input : ")
def check_palindrome(n:str )->bool :
    rev = n[::-1]
    if n == rev :
        return True
    else :
        return False
print(check_palindrome(n))

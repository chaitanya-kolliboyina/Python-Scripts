### Prob 1: Print 5 stars in line with a spaces between them

# n = int(input())
# for i in range(n):
#     print("*",end = " ")

###  Prob 2: Print 5 x 5 stars in line with a spaces between them

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#     print()

### Prob 3: Print right angle traingle with 5 rows 

# n = int(input("Enter n: "))
# for i in range(n+1):
#     for j in range(i):
#         print("*",end = " ")
#     print()

### Prob 4: Print right angle traingle with 5 rows (Right inverted form of above)

# n = int(input("Enter n: "))
# for i in range(n+1):
#     for j in range((n+1)-i-1):                                    # Controlling spaces playes major role 
#         print(" ",end = " ")
#     for k in range(i):
#         print("*", end = " ")
#     print()

### Prob 5: Print Equilateral traingle with 5 rows 

# n = int(input("Enter n: "))
# for i in range(n+1):
#     for j in range((n+1)-i-1):                                        # With spaces -> right triange ; with out spaces -> Equilateral triangle
#         print("",end = " ")                                           # Hint : Control spaces first(Here space is nothing ) and then stars
#     for k in range(i):
#         print("*", end = " ")
#     print()

### Prob 6: Print right angle traingle inverted(top - down) with 5 rows 

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range((n)-i):                                              # Hint : Control stars first and then spaces
#         print("*",end = " ")
#     print()

### Prob 7: Print right angle traingle inverted(top - down) & left right with 5 rows 

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(i):                                    # Controlling spaces playes major role 
#         print(" ",end = " ")                              # Hint: Control spaces first and then stars
#     for k in range(n-i):
#         print("*", end = " ")
#     print()

### Prob 8: Print inverted equilateral triange

# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(i):
#         print("",end = " ")
#     for j in range(n-i):
#         print("*",end =" ")
#     print()

# Prob 9: Print a kite with 9 rows

# n = int(input("Enter n: "))
# for i in range(2*n):
#     for j in range(n-i):                                     # Upper traingle
#         print("",end = " ")
#     if i<n:
#         for k in range(i):
#            print("*", end = " ")
#     else:
#         for m in range(i-n):
#             print(" ", end = "")                                    #Lower triangle
#         for l in range(2*n-i):
#             print("*",end = " ")
        
#     print()

### prob 10: Print an empty rectangle box

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         if i== 0 or i ==(n-1):
#             print("*", end = " ")
        
#         else:
#             if j ==0 or j == (n-1):
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#     print()
        
### Prob 11: Split the rectangle box into 4 equals halves

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         if i== 0 or i ==(n-1) or i == (n-1)//2:
#             print("*", end = " ")
        
#         else:
#             if j ==0 or j == (n-1) or j ==(n-1)//2:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#     print()

### prob 12: Draw a kite box 

n = int(input("Enter n: "))

for i in range(n):
    for j in range(n-i-1):
        print (" ", end = " ")
    for k in range(j):
        print("*", end = " ")
    print()

#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

time  = int(input("Enter time worked in hours: "))
per_hour = int(input("Per hour: "))
if time<=40:
    sal = per_hour * time
else:
    sal = per_hour * time * 1.5

print("Total earned: " + str(sal))

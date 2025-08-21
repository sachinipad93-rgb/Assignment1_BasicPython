
# Task 1

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number"))

add=num1 + num2 # this is for addition
sub=num1 - num2 # this is for subtraction
mul=num1 * num2 # this is for multiplication

if num2 !=0:
    div=num1 / num2
else:
    div=("Undifined (cannot divide by zero)")

print("\nHere is result:")
print("addition :", add)
print("subtraction :", sub)
print("multiplication :", mul)
print("division :", div)


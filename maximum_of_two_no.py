# write a function to find maximum of two numbers.

def maximum(a, b):
   if a > b :
     return a
   else:
     return b
     
num1 = int(input("enter your first number :"))
num2 = int(input("enter your second number :"))

print("maximum ",maximum(num1, num2))

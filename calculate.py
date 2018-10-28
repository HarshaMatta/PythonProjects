# created by harsha
# date 27/10/18
# You type in your 3 inputs.
# Using those inputs the program will determine:
#    what operation you want to use and two numbers you want to use the operation on
num1 = float(input("what is your first number"))
operation = input("what is you operation")
num2 = float(input("what is you second number"))

if operation == "/" or operation == "divide": print(num1 / num2)
elif operation == "*" or operation == "x" or operation == "times": print(num1 * num2)
elif operation == "+" or operation == "plus": print(num1 + num2)
elif  operation == "-" or operation == "minus ": print(num1 - num2)

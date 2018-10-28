# created by harsha matta
# created on 26/10/18
# this program will convert celsius to fahrenheit and vice versa
# this program takes two inputs: type of temperature you start with and the number that you want to convert
# then it output the converted temperature

def fahrenheit(number):
    print( float((number - 32) * 5 / 9 ))


def celcius(number):
    print(float((number * 9 / 5) + 32))


x = input("fahrenheit or celsius")
num = float(input("type number here"))
if x == "f" or x == "F":
    fahrenheit(num)
elif x == "c" or x == "C":
    celcius(num)
else :
    print("type f or c only")





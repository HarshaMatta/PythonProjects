# created by Harsha Matta on 4/22/19
# this is based on the Collatz-Syracuse-Ulam problem
# any number you type in for num will take you to 1
# there are 3 rules to the sequence
num = 27

print(num)
while True:

    if num%2 == 0:
        num= num/2
# rule number 1: if its even divide by 2
    elif num%2 != 0:
        num = (num*3)+1
# rule number 2: if its odd multiply by 3 and add 1
    print(int(num))

    if (num == 1):
        break
# rule number 3 : if its one the sequence will go in a infinite 4,2,1,4,2,1...
# So if the number is 1 stop the loop



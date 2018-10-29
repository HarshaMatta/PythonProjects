# by Harsha Matta
# created on 28/10/18
# You type in the answers to the questions and then it will tell you if right or not.
# It will also tell you how many questions you got right.

import random

def main():
    score = 0
    for num in range(10):

        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print(num1, "+", num2)
        ans = int(input("whats the answer"))
        if ans == num1 + num2:
            print("Correct!")
            score += 1
        else:
            print("wrong")
    print("You got", score, "of of ten questions right")

main()
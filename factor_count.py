# Created by harsha matta
# 24/10/18
# You type in your input, then the program will output the factors of all the numbers 1 to the given input number
#  Then it will output if that number is prime .
# After that the program will tell you how many primes are there from 1 to the given input number
g_onetohundred = list(range(1, int(input("type number here "))+1))

def main(list):
    prime_cnt = 0
    for num in list:

        output = []
        for factor in range(1, int(num/2) + 1):
            if num % factor == 0:
                output.append(factor)

        output.append(num)

        if len(output) == 2 :
            prime_cnt = prime_cnt + 1

            print(num, output, " Prime",)
        else:
            print(num, output)
    print("there are", prime_cnt, "primes between 1 and", num)




main(g_onetohundred)
x =input()
if x == "r" or x == "R":
    g_onetohundred = list(range(1, int(input("type number here ")) +1))
    main(g_onetohundred)




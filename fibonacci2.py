# created by harsha matta
# this code goes through the fibonacci sequence for a 100 numbers
# then it finds phi by dividing the last two fibonacci numbers
# after that it compares it to the formula of calculating them


def main():
    cnt = 0
    limit = 101
    before = 1
    twobefore = 0
    while cnt < limit:

        new = before+twobefore
        twobefore = before
        before = new
        print(new)
        cnt += 1
# finds and prints sequence

    phi= new/twobefore
# calculates using fibonacci numbers
    print("the golden ratio is", phi)
    print("and also           ",(1+5**0.5)/2)
# calculates and prints using the formula: (1+5**0.5)/2
main()
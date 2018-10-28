# by harsha matta
# created on 25/10/18
# this program takes two inputs.
#  Then it will calculate the lowest common multiple and the highest common factor of the two numbers

def IsPrime(inputNumber) :
    if inputNumber < 2 :
        return False;
    for num in range(2, inputNumber) :
        if inputNumber % num == 0:
            return False
    return True


def getPrimeNumber(inputNumber) :
    primeArr = []

    if IsPrime(inputNumber) == True :
        primeArr.append(inputNumber)
    else:
        for num in range(1, inputNumber) :
            if IsPrime(num) == True :
                primeArr.append(num)

    return primeArr


def getPrimeFactorization(inputNumber, primeArr):

    primeFactors = []
    primeIndex = 0

    factor = inputNumber
    while (factor > 0 and primeIndex < len(primeArr)) :
        if factor % primeArr[primeIndex] == 0:
            primeFactors.append(primeArr[primeIndex])
            factor = int(factor / primeArr[primeIndex])
        else:
            primeIndex = primeIndex + 1

    return primeFactors


def main(num):
    primes = getPrimeNumber(num)
#   print(primes)

    print(getPrimeFactorization(num, primes))
    return getPrimeFactorization(num, primes)


x = int(input("type number here "))
x_arr = main(x)


y = int(input("type number here "))
y_arr = main(y)

hcf_arr = []
lcm_arr = []
for num in x_arr:

    if num in y_arr:
        y_arr.remove(num)
        hcf_arr.append(num)
        lcm_arr.append(num)
    else:
        lcm_arr.append(num)


for num in y_arr:
    lcm_arr.append(num)

lcm = 1
hcf = 1

for num in hcf_arr:
    hcf = hcf * num

for num in lcm_arr:
    lcm = lcm * num

print(hcf, "is the highest common factor between", x, "and", y)

print(lcm, "is the least common multiple between", x, "and", y)
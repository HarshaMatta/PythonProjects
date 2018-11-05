# Created by Harsha Matta
# Created on 3/11/18
# Program takes a input algebraic equation (ex: 5x-2x+6y-3y+12-2).
# and then it will output the solution (ex: 3x+3y+10)

vars_dict = dict()
vars_dict["cons"] = 0

# append_to_list takes a token which is a number with a variable or a number,
#  and parses the input and stores variable and number in a dictionary.
def append_to_list(tok):

    if len(tok) > 0:
        tok = tok.lower()

        # get last character from token
        var = tok[len(tok) -1]

        # if the character is a letter
        if "a" <= var <= "z":

            # get the number from the token
            num = int(tok[0: len(tok)-1])

            # add letter as a key in the dictionary
            # and add number as a value to it
            if vars_dict.get(var) is None:
                vars_dict[var] = num
            else:
                vars_dict[var] += num
        # if it is not a letter then add this to const
        else:
            vars_dict["cons"] += int(tok)

# print_equation converts a dict to a equation format
def print_equation():
    ans = ""

    # for each key, value pair in dictionary
    for var, num in vars_dict.items():

        # if const, don't print variable, only value
        if var == "cons": var = ""

        op = "+"

        # for negative numbers, no need add operator
        if num < 0: op = ""

        # print if number is not zero.
        if num != 0:
            ans += op + str(num) + var

    print(ans)

# main divides the equation by looking for a "+" or a "-" symbol
def main():
    equation = input("algebraic equation here")
    token = ""

    # add + at the end to parse up to the end
    equation += "+"

    # for each character
    for ele in equation:

        if ele == "+" or ele == "-":
            append_to_list(token)
            token = ele
        # elif ele == "-":
        #     append_to_list(token)
        #     token = ele
        elif ele != " ":
            token += ele

    print_equation()

# call main
main()
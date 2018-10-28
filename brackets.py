#created by harsha
# created on 17/10/18

g_brackets = [ "(", "[", "]", "{", "}", ")"]

stack = []


def validate_syntax(brackets):

    index =1
    for bracket in brackets:
        if bracket== "[" or bracket == "{" or bracket == "(":
            stack.append(bracket)
        elif bracket == "]" :
            if  len(stack) == 0 or  "[" != stack.pop() :
                return "Error at ']' " +  str(index)
        elif bracket == "}" :
            if len(stack) == 0  or "{" != stack.pop() :
                return "Error at '}' " +  str(index)
        elif bracket == ")" :
            if len(stack) == 0  or "(" != stack.pop() :
                return "Error at ')' "  +  str(index)

        index = index  + 1

    return "No Error"

# implement main
def main():

    # call validation
    results = validate_syntax(g_brackets)

    # print results
    print(results)


# call main
main()
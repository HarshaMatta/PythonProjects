#created by harsha
# created on 14/10/18
# This program takes in a list of inputs
# Then it will calculate and output the mean median and mode of the inputs.

# user gives number input
g_number = []


numdict = { }


def IsArrayValid(numbers):
    if len(numbers) == 0:
        return False;
    return True;




def mode(numbers):

    if IsArrayValid(numbers) == False:
        return

    mode_dict = {}
    for key in numbers:
        cnt = mode_dict.get(key)
        if cnt == None :
            mode_dict[key] = 1
        else:
            mode_dict[key] = cnt + 1

    dict_by_val = {}
    for (key, val) in mode_dict.items():
        keylist = dict_by_val.get(val)
        if keylist == None:
            keylist = [key]
            dict_by_val[val] = keylist
        else:
            keylist.append(key)
            dict_by_val[val] = keylist

    max_key = 1
    for key in dict_by_val:
        if key > max_key:
            max_key = key

    if max_key == 1:
        return "No Mode found"
    else:
        return dict_by_val[max_key]


def median(numbers):

    if IsArrayValid(numbers) == False:
        return

    sorted_numbers = numbers
    sorted_numbers.sort();
    length = len(sorted_numbers)

    median_val = 0
    mid_len = int(length /2)
    if length % 2 == 0:
        median_val = sorted_numbers[mid_len];
        median_val += sorted_numbers[mid_len - 1];
        median_val = median_val/2;
    else:
        median_val = sorted_numbers[mid_len];

    return median_val;


def mean(numbers):
    if IsArrayValid(numbers) == False:
        return

    sum = 0
    for num in numbers:
        sum = sum + num

    meanval = sum / len(numbers)
    return meanval


def main():
    while True:
        try:
            rawval = input("Type a number, type x to calculate : ")
            if rawval == "x" or rawval == "X":
                meanval = mean(g_number)
                print("Mean = ", meanval)

                modeval = mode(g_number)
                print("Mode = ", modeval)

                medianval = median(g_number)
                print("Median ", medianval)

                break
            else:
                num = float(rawval)
                g_number.append(num)

        except ValueError:
            print("Enter only numbers")

# Execution starts here


#main()

while True :
    restartstop = input("Type r to start/restart , d to stop : ")
    if restartstop == "r" or restartstop == "R":
        main()
    if restartstop == "d" or restartstop == "D":
        break

    # calculate the 3 averages

# print the chosen average
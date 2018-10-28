g_num = [1, 2, 3, 9]
input = 12
fulNum = 0
g_num.reverse()

ten = 1

g_new_arr = []




for item in g_num:

    item = item * ten

    ten = ten * 10

    g_new_arr.append(item)

print(g_new_arr)


for num in g_new_arr:
    fulNum = fulNum + num


fulNum = input +fulNum

print(fulNum)




# this is based on the monty hall problem
# go to the link to learn what the problem is if you don't know
# https://www.youtube.com/watch?v=ggDQXlinbME

# this code will show what is the better tactic in the game

import random
goat= False
money= True
door=[goat,goat,money]
# GLOBAL VARIABLES
# ---------------------------------------------------------------------------------------------------------------------

#  IF SWITCHED WHAT WOULD HAPPEN
cnt=0
lmt=1000
correct=0
def switch(cnt,lmt,correct):
    while cnt < lmt:
        pick= random.randint(1, 3)
        if pick == 1:
            pick =3

        elif pick == 2:
            pick= 3

        else:
            pick= random.randint(1,2)

        if door[pick-1]:
            correct += 1

        cnt+=1
    print(""
          "")
    print("SWITCHED")
    print("the amount of times won when switched is: ",correct)
    print("the percentage of times won when switched is",correct/lmt*100,"%")

# this part simulates when you would switch from your original door.
# it prints your success rate
# ------------------------------------------------------------------------------------------------------------------------
# WHAT WOULD HAPPEN IF YOU KEPT YOUR ORIGINAL CHOICE

def keep(cnt,lmt,correct):
    while cnt<lmt:
        pick = random.randint(1,3)

        if door[pick-1]==True:
            correct+=1
        cnt+=1

    print("KEPT")
    print("the amount of times won when kept is: ",correct)
    print("the percentage of times won when kept is",correct/lmt*100,"%")

# this part simulates what would happen if you had kept you original choice.
# it prints your succes rate
# ----------------------------------------------------------------------------------------------------------------------
keep(cnt,lmt,correct)

switch(cnt,lmt,correct)
# calls the functions.
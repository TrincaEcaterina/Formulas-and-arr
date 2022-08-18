
# LIFT APP

# - - - - - - - - - -
# 7 | [  ] |
# 6 |      |
# 5 |      |
# 4 |      | H
# 3 |      |
# 2 |      |
# 1 |      |
# - - - - - - - - - -

# * input
# * list
# * function
# * file

# 1. call lift
# 2. destination lift
# 3. enter in lift
# 4. exit

###########################################################

from os import system
from time import sleep
import random

floor_max   = 7
floor_min   = 1

lift_floor  = random.randint(1,7)
human_floor = random.randint(1,7)
human_in_lift = False

def printFloors():
    print("- "*15)
    for floor in range(floor_max,floor_min-1, -1):
        if human_in_lift and floor == lift_floor:
            print( f"{floor} | [H ] |  " )
        elif floor == lift_floor and floor == human_floor and not human_in_lift:
            print( f"{floor} | [  ] |  H" )   
        elif floor == human_floor and not human_in_lift:
            print( f"{floor} |      |  H" )
        elif floor == lift_floor:
            print( f"{floor} | [  ] | " )  
        else:
            print( f"{floor} |      |" )

    print("- "*15)

def printMenu():
    print("1. call lift")
    print("2. destination lift")
    print("3. enter in lift")
    print("4. exit")
    options = int(input(">>>>>>>"))
    return options


def call():
    # call works only DOWN
    # HW1: if / else --> DOWN / UP
    global lift_floor
    while True:
        if lift_floor < human_floor:
            sleep(0.5)
            lift_floor += 1
            system("clear")
        elif lift_floor > human_floor:
            sleep(0.5)
            lift_floor -= 1
            system("clear")
        else:
            break
        printFloors()
      

# HW2: if/else 

def destionation():
    global lift_floor
    where_to = int(input("Wich floor: "))
    while lift_floor != where_to:
        if where_to < lift_floor:
            sleep(0.5)
            lift_floor -= 1
        elif where_to > lift_floor:
            sleep(0.5)
            lift_floor += 1
        system("clear")
        printFloors()  


def enter():
    global human_in_lift
    if lift_floor == human_floor:
        human_in_lift = True
    else:
        print("WARNING, You can fall!") 

def exit():
    global human_in_lift, human_floor
    if human_in_lift:
        human_in_lift = False
        human_floor = lift_floor

    else:
        print("WARNING, human not in lift!") 



###########################################################

while True:
    system("clear")
    printFloors()
    printMenu ()
    option = printMenu()
    if option == 1:
        call()
    elif option == 2:
        destionation()
    elif option == 3:
        enter()
    elif option == 4:
        exit()
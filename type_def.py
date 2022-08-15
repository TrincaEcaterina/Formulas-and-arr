from email import message
from os import system

mesage = []

system("clear")
def inputInt(mesage):
    value = int(input("Enter some value: "))
    mesage.append(value)
    print(mesage)

def inputFloat(mesage):
    value = float(input("Enter some value: "))
    mesage.append(value)
    print(mesage)

def inputBoolean(mesage):
    value = bool(input("Enter some value: "))
    mesage.append(value)
    print(mesage)

inputInt(mesage)
inputFloat(mesage)
inputBoolean(mesage)

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")

print( n + m )

    
    
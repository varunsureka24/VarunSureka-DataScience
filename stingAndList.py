# Varun Surela 
# 1/13/22
# learning about strings and lists

# import os, sys, random

# os.system('cls')

# num1 = 8
# num2 = 4.5
# char = 't'
# flag = False
# StringVar1= 'Hello There'
# StringVar2 = 'Goodbye There'

# #concatanation
# print(StringVar1 +" "+ StringVar2)
# print(StringVar1 +" "+ str(num1) + " " + StringVar2)

# print(type(num2))   
# print(StringVar1[0])

# print("hello \t peter \n i am here \\ or not \"goodbye\"")

# for letter in StringVar1:
#     print(letter, end ="")
# print()
# for i in range(8):
#     print(i)
# print()
marioSize = input("what size would you like the tower: ")
size = int(marioSize)

while size < 0:
        marioSize = input("what size would you like the tower: ")
        size = int(marioSize)

for i in range(size, 0, -1):
    for spaces in range(i - 1, 0, -1):
        print(" ", end="")
    for star in range(0,(size - i), 1):
        print("*", end="")
    print("  ",end = "")
    for star in range(0,(size - i), 1):
        print("*", end="")
    for spaces in range(i - 1, 0, -1):
        print(" ", end="")
    print()
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
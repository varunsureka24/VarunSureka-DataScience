
while True:
    marioSize = input("what size would you like the tower: ")
    size = int(marioSize) + 1
    if (size == 0):
        print("goodbye, thank you for playing")
        break
    if (size < 2 or size > 26):
        print("bad number")
    else:
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
    
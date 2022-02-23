# Varun Sureka from Maria Suarez
# 02/08/2022 

#Create word lists
import os, random, requests, json

os.system('clear')
word=""
guess=""

res = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")
dictionary = res.json()

words = dictionary.keys()
# print(type(words))
# print(words)
word5 = []
word4 = []
word3 = []

def selectWord():
    global word
    for i in words:
        if len(i) == 3:
            word3.append(i)
        if len(i) == 4:
            word4.append(i)
        if len(i) == 5:
            word5.append(i)

gameOn=True
tries=0
letterGuessed=""
selectWord()

diff = input("enter difficulty: ")

# print(len(word3))
# print(len(word4))
# print(len(word5)) 

if diff == '3':
    length = 3
    ran = random.randint(0,936)
    word = word3[ran]
elif diff == '4':
    length = 4
    ran = random.randint(0,3530)
    word = word4[ran]
elif diff =='5':
    length = 5
    ran = random.randint(0,6371)
    word = word5[ran]
else:
    print("please enter a number 3 - 5")

# print(word)

def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")


while gameOn:
   
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n Sorry run out chances ")
        #playGame() ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed! ")
        #Calculate score
        #playGame()
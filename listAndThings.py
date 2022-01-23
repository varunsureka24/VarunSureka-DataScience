#01/20/22
import os
os.system('clear')
#learning about list,tuples, dictionaries, etc

fruits = ['apples, oranges', 1,7, 'banana']
print(len(fruits))

for elem in fruits:
    print(type(elem))

mylist = ((3,5,6))
print(mylist)

fruits.append('kiwi')
fruits.insert(3,'grapes')
print(fruits)
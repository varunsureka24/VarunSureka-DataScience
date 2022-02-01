#Varun Sureka
#1/31/2022
#Editing diversity school CSV

import os
import csv
os.system('clear')

#Analyze the data set and describe some studies you could do with this data. If any bad data or values that would need to be replaced?
#Remove data with NA as state
#Can compare percentages of populations of minorities within schools and states

file = open('diversity_school.csv')
divFile = csv.reader(file)
header = next(divFile)
states = [] #states of colleges
divList = [] #just the data from the file stored in an array
for row in divFile:
    divList.append(row)

for row in divList:
    if row[2] not in states and row[2] != 'NA': #this makes sure that only new states populate the states array
        states.append(row[2]) #it is [2] because that is the position of the state in divList and in the original csv file

#Make a list of all the minority groups per state and add a total number of students
length = len(states)
for state in range(length): #iterates per state
    minorityGroups = [] #only minorities populate this array
    totalMinorities = 0
    for row in divList: #iterates over the entire file
        if states[state] == row[2]: #this checks to see if the state in the CSV file matches the state we are counting for. This prevents recounting
            if row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'White' and row[3] != 'Unknown' and row[3] != 'Non-Resident Foreign' and row[3] not in minorityGroups:
                minorityGroups.append(row[3]) #This checks to make sure that the person is a unqiue minorty by eliminating anything they cannot be.
            if row[3] == 'Total Minority': 
                totalMinorities += int(row[4]) #total minority is the number of minorities in this college. #this adds the value to totalMinorities
    print(str(states[state]) + ' contains a total minority population of', str(totalMinorities) + ' including groups: ', end = '')
    print(minorityGroups) #prints out the minority groups
print()

#Make a list of the number of schools studied per state
for state in range(length): #iterates per state
    schools = [] #array for each school
    for row in divList:
        if row[2] == states[state] and row[0] not in schools: #if it is a unique school in the right state
            schools.append(row[0]) #appended to array
    print(str(states[state]) + ' contains ' + str(len(schools)) + ' schools') #prints number of schools per state
print()

#What is the greatest ethnic group per state
for state in range(length):
    groups = [] #contains the various different groups
    groupcounts = [] #contians the number of people in each group
    for row in divList:
        if row[2] == states[state] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] not in groups:
            groups.append(row[3]) #appends unique minority groups
            groupcounts.append(0) #makes sure that groupcounts is the right size
    for i in range(len(groups)): #for each group
        for row in divList:
            if row[2] == states[state] and row[3] == groups[i]: #if it is in the right state and right group, then add the number of minorities
                groupcounts[i] += int(row[4])
    print(states[state] + '\'s largest ethinicity population enrolled in university is ' + str(groups[groupcounts.index(max(groupcounts))]) + ' at ' + str(max(groupcounts)))

print()
#Add a column for a percentage of race per university
# universities = []
# for row in divList:
#    if row[0] not in universities:
#        universities.append(row[0]) #array of unique universities

# for school in range(len(universities)):
#    population = 0
#    for row in divList:
#        if row[0] == universities[school]:
#            population += int(row[4]) #sums the total population of enrollment at any school
#    for row in divList:
#        if row[0] == universities[school] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'Unknown': #checks to make sure its the right type of category
#            print(universities[school] + ' is ' + str(round(int(row[4])/population, 2) * 100) + '% ' + row[3])
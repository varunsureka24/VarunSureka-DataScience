#Varun Sureka
#01/24/2022
#
#Preparing Data Sets
import csv, os

os.system('clear')

file = open('insurance_data - insurance.csv')
insuranceFile = csv.reader(file)

header = next(insuranceFile)

insuranceData = []


for row in insuranceFile:
    insuranceData.append(row)

for row in insuranceData:
    if row[1] == 'female':
        row[1] = 0
    if row[1] == 'male':
        row[1] = 1


for row in insuranceData:
    if row[4] == 'no':
        row[4] = 0
    if row[4] == 'yes':
        row[4] = 1

for row in insuranceData:
    insurance_cost = 250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]) + 24000*int(row[4]) - 12500
    insurance_cost = int(insurance_cost*100)/100
    row.append(insurance_cost)

Southwest_Total = 0 
Northeast_Total = 0 
Southeast_Total = 0
Northwest_Total = 0
countNE = 0 
countSE = 0
CountNW = 0
CountSW = 0


for row in insuranceData:
    if row[5] == 'northeast':
        Northeast_Total += row[7] 
        countNE +=1
        NE_AVG = Northeast_Total/countNE
    if row[5] == 'southeast':
        Southeast_Total += row[7] 
        countSE +=1
        SE_AVG = Southeast_Total/countSE
    if row[5] == 'northwest':       
        Northwest_Total += row[7] 
        CountNW += 1
        NW_AVG = Northwest_Total/CountNW
    if row[5] == 'southwest':
        Southwest_Total += row[7] 
        CountSW += 1
        SW_AVG = Southwest_Total/CountSW

Region_AVG = [NE_AVG, SE_AVG, NW_AVG, SW_AVG]

List_Female = []
List_Male = []

for row in insuranceData:
    if row[1] == 'female':
        List_Female.append(row)
    if row[1] == 'male':
        List_Male.append(row)

List_Smokers  = []
List_NonSmokers = []


for row in insuranceData:
    if row[4] == 'no':
        List_NonSmokers.append(row)
    if row[4] == 'yes':
        List_Smokers.append(row)
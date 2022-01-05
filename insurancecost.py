#base variables. information about the women
age = 28
new_age = age + 4 #lookign at age factor
sex = 0
new_sex = 1 #male v female factor
bmi = 26.2
new_bmi = bmi + 3.1 #lookign at bmi factor
num_of_children = 3
new_num_of_children = num_of_children + 2 #lookign at num_of_children factor
smoker = 0
new_smoker = 1 #if smoker

#working with the formula
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
#lookign at age factor
new_insurance_cost = 250*new_age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 #if the age is older
change_in_insurance_cost = new_insurance_cost - insurance_cost #differnece in insurance cost

#bmi factor
new_insurance_cost2 = 250*age - 128*sex + 370*new_bmi + 425*num_of_children + 24000*smoker - 12500 #if the bmi is more
change_in_insurance_cost2 = new_insurance_cost2 - insurance_cost #differnece in insurance cost

#male v female factor
new_insurance_cost3 = 250*age - 128*new_sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 #if the bmi is more
change_in_insurance_cost3 = new_insurance_cost3 - insurance_cost #differnece in insurance cost

#lookign at num_of_children factor
new_insurance_cost4 = 250*age - 128*sex + 370*bmi + 425*new_num_of_children + 24000*smoker - 12500 #if the bmi is more
change_in_insurance_cost4 = new_insurance_cost4 - insurance_cost #differnece in insurance cost

#if smoker
new_insurance_cost5 = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*new_smoker - 12500 #if the bmi is more
change_in_insurance_cost5 = new_insurance_cost5 - insurance_cost #differnece in insurance cost

#print
print("This person's insurance cost is " + str(insurance_cost) + " dollars")
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost2) + "dollars.")
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost3) + " dollars")
print("The change in estimated cost for havng 5 children is " + str(change_in_insurance_cost4) + " dollars")
print("The change in estimated cost for being smoking is " + str(change_in_insurance_cost5) + " dollars")

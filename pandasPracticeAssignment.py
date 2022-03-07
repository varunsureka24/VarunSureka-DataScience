# -*- coding: utf-8 -*-
import pandas as pd 
import os
os.system('clear')

#Store DF
StoreListColumns = ['Product ID', 'Product Name', 'Color']
StoreList = [[1,'San Diego', 100],[2,'Los Angeles', 120],[3,'San Francisco', 90], [4,'Sacramento', 115]]
df2 = pd.DataFrame(StoreList, columns= StoreListColumns)

#Wardrobe DF
WardrobeColumns = ['Product ID', 'Product Name', 'Colors']
WardrobeList = [[1,'T-Shirt', 'Blue'],[2,'T-Shirt','Green'],[3,'skirt','red'],[4,'skirt', 'black']]
df1 = pd.DataFrame(WardrobeList, columns= WardrobeColumns)

#Insurance Data
InsuranceDF = pd.read_csv('insurance_data.csv', encoding = "utf-8" )

InsuranceDF['sex'].replace(to_replace = 'female', value = 0,inplace=True)
InsuranceDF['sex'].replace(to_replace = 'male', value = 1,inplace=True)
InsuranceDF['smoker'].replace(to_replace = 'no', value = 0,inplace=True)
InsuranceDF['smoker'].replace(to_replace = 'yes', value = 1,inplace=True)

insurance_cost = 250*(InsuranceDF['age']) - 128*(InsuranceDF['sex']) + 370*(InsuranceDF['bmi']) + 425*(InsuranceDF['children']) + 24000*(InsuranceDF['smoker']) - 12500

InsuranceDF['cost'] = insurance_cost


#DF to CSV FIle
df1.to_csv('PandasWardrobe.csv')
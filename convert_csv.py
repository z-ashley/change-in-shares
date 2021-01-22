import pandas as pd 
import numpy as np 


# Reading the csv file 
df_new = pd.read_csv('arkg_holdings.csv') 

# saving xlsx file 
GFG = pd.ExcelWriter('arkg_holdings.xlsx') 
df_new.to_excel(GFG, index = False) 

GFG.save() 

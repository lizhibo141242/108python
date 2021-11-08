import os.path
import pandas as pd 
df=pd.read_excel(r'D:\108python\莉莉.xls') 
df
print('外交部=',df.iloc[4,12])
os.getcwd()


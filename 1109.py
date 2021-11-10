import os.path
import pandas as pd 
df=pd.read_excel(r'D:\108python\sample1.xlsx',header=None) 
total=df.loc[df[0]=='总计']

row={}
row['员工ID']=df.iloc[3,7]
row['姓名']=df.iloc[3,1]
row['开始时间']=df.iloc[0,7]
row['结束时间']=df.iloc[0,9]
row['酒店费用']=total.iloc[0,3]
row['交通费']=total.iloc[0,4]
row['油费']=total.iloc[0,5]
row['餐饮']=total.iloc[0,6]
row['电话']=total.iloc[0,7]
row['招待费']=total.iloc[0,8]
row['杂项']=total.iloc[0,9]
row['总计']=total.iloc[0,10]

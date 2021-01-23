import pandas as pd 
import numpy as np
from pandas import Series, DataFrame
account=pd.read_csv(r'D:\tools\radius-20210122\radius-7\radius-7\78.txt',encoding='ANSI')
"""
print(account)
print(account.head())
account.info()
"""
#改列名
account.columns = ['pppoe','1','2','3','4','5','6','7','8','9','10','11','mac','13']
account.info()

#去掉pppoe和mac列中的无关字符，只保留帐号和MAC地址
#onuggl['MAC地址 / SN']=onuggl['MAC地址 / SN'].str.replace(":","")
account['pppoe']=account['pppoe'].str.replace('net_no','')
account['pppoe']=account['pppoe'].str.replace('[','')
account['pppoe']=account['pppoe'].str.replace('{','')
account['pppoe']=account['pppoe'].str.replace('"":"','')
account['pppoe']=account['pppoe'].str.replace('"','')
account['mac']=account['mac'].str.replace('calling_station_id:','')
account['mac']=account['mac'].str.replace('"','')
account['mac']=account['mac'].str.replace(':','')
print(account.head())

#去重操作
account = account.drop_duplicates(subset=['pppoe','mac'])
print(account)
#保存'pppoe'和'mac'两列
account1 = account[['pppoe','mac']]
print(account1)
account1.to_csv('pppoe_mac.csv')
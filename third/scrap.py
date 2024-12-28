import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

r=requests.get(url)
# print(r.text)

soup=BeautifulSoup(r.text,'lxml')
# print(soup)

data=soup.find_all('h4',{"class":"float-end price card-title pull-right"})
# print(len(data.text))'

l=[i.text for i in data]

# print(len(l))

data1=soup.find_all('p',{"class":"description card-text"})

l1=[i.text for i in data1]

print(l1)


import pandas as pd

df=pd.DataFrame(zip(l,l1),columns=['Price','Description'])

print(df)

df.to_csv('laptopdata.csv',mode='a',index=False)
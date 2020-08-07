# coding: utf-8
#web scrapping with bs4
#scrapping on the imdb page 
import requests
from bs4 import BeautifulSoup
url='https://www.imdb.com/list/ls024149810/'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')

movies_title=[]
for title in soup.findAll('h3',{'class':'lister-item-header'}):
    titles=title.find('a').get_text()
    movies_title.append(titles)
    

import pandas as pd
topmovies=pd.DataFrame({
    'Movie_Title':movies_title
})

print(topmovies)







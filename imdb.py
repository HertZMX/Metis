# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 00:15:13 2022

@author: hertz
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

#create empty arrays to store info
TitleName=[] 
Year=[] 
Certificate=[]
PlayTime=[]
Genre=[]
Rating=[]
Metastone=[]
Director=[]
Stars=[]
Vote=[]

#extract info from the URL
url = "https://www.imdb.com/search/title/?year=2022&title_type=feature&"
r = requests.get(url).content

soup = BeautifulSoup(r, "html.parser") 
movies = soup.find("div",{"class":"lister-list"}).find_all("div",{"class":"lister-item mode-advanced"})

#loop to scrap all the info
for i in movies:

    title = i.find("h3",{"class":"lister-item-header"})
    year = i.find("span",{"class":"lister-item-year text-muted unbold"})
    cert = i.find("span",{"class":"certificate"})
    playtime = i.find("span",{"class":"runtime"})
    genre = i.find("span",{"class":"genre"})
    metastone = i.find("span",{"class": "metascore  favorable"})
    
    TitleName.append(title.text)
    Year.append(year.text)
    Certificate.append(cert.text)
    PlayTime.append(playtime.text)
    Genre.append(genre.text)
    Metastone.append(metastone.text)
    
#create a dataframe to store all of the info
df=pd.DataFrame({'Title' : TitleName,'year':Year,'Certificate':Certificate,
                 'PlayTime':PlayTime,'Genre':Genre,"Metastone":Metastone})

df.head()


#!/usr/bin/env python
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup
import requests
from csv import writer
from scipy.stats import mannwhitneyu


# In[2]:


url = "https://www.kinopoisk.ru/lists/movies/top250/"


# In[3]:


page = requests.get(url)


# In[4]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[5]:


lists = soup.find_all('div',class_ = "styles_root__ti07r" )


# In[6]:


with open('Movie_rating.csv', 'w', encoding = 'utf8', newline ='') as f:
    thewriter = writer(f)
    header = ['Ranking', 'Title in English', 'Title in Russian', 'Info', 'new_Rating', 'old_Rating', 'Views']
    thewriter.writerow(header)
    
    for list in lists:
        Ranking = list.find('span', class_ = "styles_position__TDe4E").text.replace('\n', '')
        title_eng = list.find('a',class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text.replace('\n', '')
        title_rus= list.find('div',class_='styles_content__nT2IG').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        info = list.find('span', class_ = "desktop-list-main-info_truncatedText__IMQRP").text.replace('\n', '')
        new_rating = list.find('div', class_ = "styles_rating__ni2L0 styles_root___s7Tg styles_rootMd__ZvdRj styles_rootPositive__PIwO2").text.replace('\n', '')
        old_rating = list.find('span', class_ = "styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg").text.replace('\n', '')
        views= list.find('div',class_='styles_user__2wZvH').find('div',class_='styles_rating__LU3_x').find('span',class_='styles_kinopoiskCount__2_VPQ').text.replace('\n','')
        info = [Ranking,title_eng, title_rus, info, new_rating, old_rating, views]
        thewriter.writerow(info)


# In[7]:


import pandas as pd


# In[9]:


movies = pd.read_csv('Movie_rating.csv')


# In[10]:


movies.head()


# In[11]:


movies


# In[12]:


movies.info


# In[14]:


movies.truncate(before = 0, after = 29)


# In[17]:


mannwhitneyu(movies['new_Rating'], movies['old_Rating'])


# In[20]:


# We cannot reject the hypothisis because there is a statistical difference between old and new ratings.


# In[ ]:





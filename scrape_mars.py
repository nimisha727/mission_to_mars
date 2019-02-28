#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import requests
import pymongo
import pandas as pd
import time


# In[2]:


#GETTING HEADLINES AND PARAGRAPH OF LATEST NEWS:


# In[3]:


#pointing to the directory where chromedriver exists
executable_path = {'executable_path':"C:\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)
time.sleep(2)


# In[4]:


# Visit mars.nasa.gov/news/
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)

# Scrape page into Soup
news_html = browser.html
news_soup = BeautifulSoup(news_html, "html.parser")


# In[5]:


# Get the headlines
head_lines= news_soup.find('div', class_='content_title').text  

# Get the paragraph for the headlines
para_text = news_soup.find('div', class_='article_teaser_body').text 


# In[6]:


print(head_lines)
print("-----------------")
print(para_text)


# In[7]:


#GETTING THE IMAGE OF THE CURRENT HOME PAGE:


# In[8]:


#pointing to the directory where chromedriver exists
executable_path = {'executable_path':"C:\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:



# URL of page to be scraped
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)
time.sleep(2)
# Scrape page into Soup
image_html = browser.html
image_soup = BeautifulSoup(image_html, "html.parser")
time.sleep(2)


# In[10]:


#Navigate to link to find details
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)


# In[11]:


#Navigate to link to find details
browser.click_link_by_partial_text('more info')
time.sleep(2)

# getting the code from the page:
img_html = browser.html

#Scrape the page into soup:
img_soup = BeautifulSoup(img_html,'html.parser')

#Finding the path from the soup:
img_path = img_soup.find('figure' , class_='lede').a['href']
featured_image_url = "https://www.jpl.nasa.gov" + img_path


# In[12]:


featured_image_url


# In[13]:


#Mars weather


# In[14]:


#pointing to the directory where chromedriver exists
executable_path = {'executable_path':"C:\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# In[15]:



# URL of page to be scraped
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)
time.sleep(2)

# Scrape page into Soup
weather_html = browser.html
weather_soup = BeautifulSoup(weather_html, "html.parser")
time.sleep(2)


# In[16]:


#Collecting weather information:
mars_weather = weather_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print("Mars weather")
print("------------")
print(mars_weather)


# In[17]:


#MARS FACTS:


# In[18]:


#pointing to the directory where chromedriver exists
executable_path = {'executable_path':"C:\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


#Using pandas to convert the data to a HTML table string:
table_lst = pd.read_html('http://space-facts.com/mars/')
print(table_lst)


# In[20]:


#Converting the list into dataframe:
facts_df = table_lst[0]
facts_df.columns=["Parameters","Values"]
facts_df.head()


# In[21]:


#Converting the dataframe to html string
html_string = facts_df.to_html()
print(html_string)


# In[22]:


### Mars Hemispheres


# In[69]:


#pointing to the directory where chromedriver exists
executable_path = {'executable_path':"C:\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# In[70]:



# URL of page to be scraped
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)
# Scrape page into Soup
hemi_html = browser.html
hemi_soup = BeautifulSoup(hemi_html, "html.parser")


# In[71]:


# Iterate through all pages
#for x in range(5):
    # HTML object
hemi_html = browser.html
    # Parse HTML with Beautiful Soup
hemi_soup = BeautifulSoup(hemi_html, 'html.parser')
   # Retrieve all elements that contain title information
titles = hemi_soup.find_all('h3')

titley = []
    # Iterate through each title
for title in titles:
    titlex = title.text.strip()
    titley.append(titlex)


# In[72]:


type(titley)


# In[79]:


hemi_titles_urls = []

for y in titley:
    try:
        # Identify and return url of the image
        browser.click_link_by_partial_text(y) 
        
        next_page_soup = BeautifulSoup(browser.html, "html.parser")
        hemi_urls = browser.find_by_id('wide-image').find_by_tag('a')
        blah = hemi_urls['href']
        print(" -> hemi_urls: ", blah)
        browser.back()
        print(y)
        blah2 = {"image title": y, "image_url" : blah}
#        blah2 = {y: blah}
        hemi_titles_urls.append(blah2)
    except AttributeError as e:
        print('ERROR: ', e)


# In[80]:


hemi_titles_urls


# In[28]:


mars_info_dict = {
    "head_lines": head_lines,
    "para_text": para_text,
    "featured_image": featured_image_url,
    "mars_weather": mars_weather,
    "mars_facts": html_string
    }


# In[29]:


type(mars_info_dict)


# In[30]:


print(mars_info_dict)


# In[31]:


# Module used to connect Python with MongoDb
import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'marsdb' database in Mongo
db = client.marsdb

# Insert a document into the 'info' collection
db.info.insert_one(
    {
    "head_lines": head_lines,
    "para_text": para_text,
    "featured_image": featured_image_url,
    "mars_weather": mars_weather,
    "mars_facts": html_string
    }
)


# In[83]:


db.info.insert(hemi_titles_urls)


# In[ ]:





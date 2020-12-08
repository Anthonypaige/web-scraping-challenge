#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all dependencies
import time
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint


# In[2]:


# Function to choose the executable path to driver
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# In[3]:


# Run init_browser/driver.
browser = init_browser()

# Visit Nasa news url.
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)

# HTML Object.
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)


# In[7]:


# Run init_browser/driver.
browser = init_browser()

# Visit the url for JPL Featured Space Image.
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)

# HTML object
html = browser.html

# Parse with Beautiful Soup 
soup = BeautifulSoup(html, "html.parser")

image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image

print(featured_image_url)


# In[8]:


#Visit the url for Mars facts
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)

# Use Panda's `read_html` to parse the URL.
mars_data = pd.read_html(facts_url)

#Use Pandas to convert the data to a HTML table string.
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)


# In[9]:


# Create list of dictionaries called hemisphere_image_urls.
# Iterate through all URLs saved in hemis_url.
# Concatenate each with the main_astrogeo_url.
# Confirm the concat worked properly: confirmed.
# Visit each URL.

import time 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})


# In[11]:


mars_hemisphere


# In[ ]:





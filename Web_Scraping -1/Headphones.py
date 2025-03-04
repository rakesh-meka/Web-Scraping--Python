from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/headphones/s?k=headphones"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
 html_content = response.text
else:
 print("Fetching Error", response.status_code)

soup = BeautifulSoup(html_content, 'lxml')

#print(soup)

product_title = soup.find_all('div', class_  ="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")
title = []
for i in product_title[0:20]:
   d = i.get_text()
   title.append(d)

#print(title)

product_price = soup.find_all('span', class_ = "a-price-whole")
price = []
for i in product_price[0:20]:
  d = i.get_text()
  price.append(d)

#print(price)

import re

product_reviews = soup.find_all('div', class_="a-row a-size-small")
reviews = []

for i in product_reviews[0:20]:
    d = i.get_text().strip()
    
    # Remove the numbers and commas at the end of the string
    d = re.sub(r'\s\d{1,3}(?:,\d{3})*(?=\s*$)', '', d)  # Regex to remove numbers like 19,094 at the end
    
    reviews.append(d)

#print(reviews)


no_of_reviews = soup.find_all('span', class_ = "a-size-base s-underline-text")
total_reviews = []
for i in no_of_reviews[0:20]:
  d = i.get_text()
  total_reviews.append(d)
  
#print(total_reviews)

images = soup.find_all('div', class_ = "a-section aok-relative s-image-fixed-height")
image = []
for i in images[0:20]:
  d = i.img['src']
  image.append(d)

#print(image)

import pandas

data = { "product_title": pandas.Series(title),
         "product_price": pandas.Series(price),
         "product_reviews":pandas.Series(reviews),
         "no_of_reviews":pandas.Series(total_reviews),
         "images":pandas.Series(image)
}

print(data)
df = pandas.DataFrame(data)
df.to_csv("Headphones_info.csv", encoding = 'utf-8', index= False)









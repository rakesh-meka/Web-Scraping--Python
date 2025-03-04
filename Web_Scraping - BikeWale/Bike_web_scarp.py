import requests
import pandas
from bs4 import BeautifulSoup


response = requests.get("https://www.bikewale.com/new-bike-launches/")
print(response)
soup = BeautifulSoup(response.content,"html.parser")

names = soup.find_all('span', class_= "o-cJrNdO o-bkmzIL o-eqqVmt o-fzpibr" )
name = []
for i in names[0:20]:
   d = i.get_text()
   name.append(d)
  

prices = soup.find_all('span', class_= "o-cJrNdO o-byFsZJ o-bkmzIL o-bVSleT" )
price = []
for i in prices[0:20]:
   d = i.get_text()
   price.append(d)
  

launched_date = soup.find_all('p', class_= "o-zmksK o-eemiLE o-fzpihx o-fzptYC" )
date = []
for i in launched_date[0:20]:
   d = i.get_text()
   date.append(d)

bike_spec = soup.find_all('span', class_= "o-cNwRuH o-cQa-DfF")
specification = []
for i in bike_spec[0:20]:
   d = i.get_text()
   specification.append(d)
   
images = soup.find_all('img', class_ = "o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI")
image = []
for i in images[0:20]:
   d = i['src']
   image.append(d)

data = {"Names": pandas.Series(name),
        "Prices": pandas.Series(price),
          "Launched_date": pandas.Series(date),
            "Bike_spec": pandas.Series(specification),
              "Images": pandas.Series(image)}
print(data)
df = pandas.DataFrame(data)
df.to_csv("Bike_Data.csv")
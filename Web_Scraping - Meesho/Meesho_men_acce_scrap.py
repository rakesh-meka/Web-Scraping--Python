import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://www.meesho.com/accessories-men/pl/3tp")

soup = BeautifulSoup(response.content,"html.parser")
#print(soup)

names = soup.find_all('p', class_ = "sc-eDvSVe gQDOBc NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU")
name = []
for i in names[0: 33]:
    d = i.get_text()
    name.append(d)



prices = soup.find_all('div', class_ = "sc-ftTHYK ijCOEg NewProductCardstyled__PriceRow-sc-6y2tys-7 aLtVl NewProductCardstyled__PriceRow-sc-6y2tys-7 aLtVl")
price = []
for i in prices[0: 33]:
    d = i.get_text()
    price.append(d)
#print(price)

ratings = soup.find_all('span', class_ = 'sc-eDvSVe laVOtN')
rate = []
for i in ratings[0: 33]:
    d = i.get_text()
    rate.append(float(d))
#print(rate)


reviews = soup.find_all('span', class_ = "sc-eDvSVe XndEO NewProductCardstyled__RatingCount-sc-6y2tys-22 iaGtYc NewProductCardstyled__RatingCount-sc-6y2tys-22 iaGtYc")
review  = []
for i in reviews[0:33]:
    d = i.get_text()
    review.append(d)
    #print(review)

links = soup.find_all('div', class_ = "sc-dkrFOg ProductList__GridCol-sc-8lnc8o-0 cokuZA eCJiSA")
link = []
for i in links[0:33]:
    d = "https://www.meesho.com"+i.a['href']
    link.append(d)
    #print(link)

images = soup.find_all('div', class_ = "NewProductCardstyled__ProductImage-sc-6y2tys-19 czNIkn")
image = []
for i in images[0:33]:
    d = i.img['src']
    image.append(d)
    #print(image)

data = { 'Names':pandas.Series(name),
        'Prices':pandas.Series(price),
        'Ratings':pandas.Series(rate),
        'Reviews':pandas.Series(review),
        'Links':pandas.Series(link),
        'Images':pandas.Series(image),
}
print(data)
df = pandas.DataFrame(data)
df.to_csv("Meesho_Men_Accessories_main01.csv", encoding = 'utf-8', index= False)

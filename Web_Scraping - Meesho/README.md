# Meesho Men Accessories 

## Overview

This project is a Python web scraping script designed to extract product details from the "Men Accessories" category on Meesho, an e-commerce platform. The script gathers product names, prices, ratings, reviews, product links, and images, and saves the extracted data into a CSV file for further analysis or usage.

### Data Collected
The script collects the following data for each product listed under the Men Accessories section on Meesho:

- **Names**: Product names (titles)
- **Prices**: Product prices
- **Ratings**: Product ratings (out of 5)
- **Reviews**: Number of reviews
- **Links**: Direct links to the product pages
- **Images**: Image URLs for the product images

This data is then saved into a CSV file (`Meesho_Men_Accessories_main01.csv`), which can be opened in any data analysis tool or spreadsheet application.

## Requirements

To run this script, you need to have the following Python libraries installed:

- `requests` for making HTTP requests
- `beautifulsoup4` for parsing HTML content
- `pandas` for storing and manipulating the data

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4 pandas

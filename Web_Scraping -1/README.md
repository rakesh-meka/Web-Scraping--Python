# Amazon Headphones Data Scraper

This project scrapes real-time data from Amazon's headphone product page. The scraped data includes product titles, prices, reviews, number of reviews, and product images. The data is then stored in a CSV file for further analysis.

## Table of Contents
- [Overview](#overview)
- [Tools Used](#tools-used)
- [How the Scraper Works](#how-the-scraper-works)
- [Installation](#installation)
- [Result](#result)
- [License](#license)

## Overview

This project demonstrates how to use web scraping techniques to extract product information from Amazon's website. Specifically, the scraper focuses on the headphone section. The scraped information includes:

- **Product Title**: The title of the headphone product.
- **Product Price**: The price of the product.
- **Product Reviews**: Review ratings of the product.
- **Total Reviews**: The total number of reviews for the product.
- **Product Images**: The image URLs of the product.

The scraped data is saved into a CSV file called `Headphones_info.csv`.

> **Note**: This project is intended for educational purposes only and demonstrates how web scraping can be used for data collection. It is not intended for commercial use. Always ensure that scraping websites complies with their terms of service.

## Tools Used

- **Python**: The primary language used to create the scraper.
- **BeautifulSoup**: A Python library used for parsing HTML and XML documents.
- **Requests**: A simple HTTP library for making requests to the website.
- **Pandas**: A data manipulation library used to organize the scraped data and save it into a CSV file.
- **Regex (Regular Expressions)**: Used to clean and process certain parts of the scraped data.

## How the Scraper Works

The scraper works as follows:

1. **Request Data**: The script sends an HTTP request to the Amazon headphone product page, passing a user-agent header to mimic a real browser request.
   
2. **Parse the HTML**: Once the response is received, the HTML content of the page is parsed using BeautifulSoup.
   
3. **Extract Data**:
   - The script extracts various pieces of data such as product titles, prices, reviews, and image URLs from the HTML.
   - It uses CSS classes to target the specific elements containing this information.

4. **Clean Data**: Some of the extracted data, like reviews and prices, might need cleaning (e.g., removing unnecessary characters like "M.R.P." or numbers at the end). This is handled with **Regular Expressions**.

5. **Save Data**: The cleaned data is stored in a Pandas DataFrame, which is then saved to a CSV file, `Headphones_info.csv`.

6. **Output**: The output CSV contains the following columns:
   - `product_title`: Title of the product.
   - `product_price`: Price of the product.
   - `product_reviews`: Review ratings of the product.
   - `no_of_reviews`: Total number of reviews for the product.
   - `images`: Image URLs for the product.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/amazon-headphones-scraper.git
    cd amazon-headphones-scraper
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    > **Note**: You may need to install the following packages manually if they aren't in the `requirements.txt` file:
    - `beautifulsoup4`
    - `requests`
    - `pandas`
    - `lxml`
    - `re` (Regular Expressions module, built into Python)

3. Run the script:

    ```bash
    python scrape_headphones.py
    ```

    This will scrape the Amazon webpage and save the data into `Headphones_info.csv`.

## Result

Once the script is executed, it will generate a CSV file (`Headphones_info.csv`) with the following columns:

- **product_title**: Title of the headphone product.
- **product_price**: Price of the product.
- **product_reviews**: Review rating of the product.
- **no_of_reviews**: Total number of reviews.
- **images**: Image URLs for the product.

The CSV file will look something like this:

| product_title                | product_price | product_reviews | no_of_reviews | images             |
|------------------------------|---------------|-----------------|---------------|--------------------|
| XYZ Headphone 1               | ₹1,499        | 4.5 out of 5    | 1,200         | `image_url_1.jpg`  |
| XYZ Headphone 2               | ₹2,499        | 4.2 out of 5    | 850           | `image_url_2.jpg`  |
| ...                          | ...           | ...             | ...           | ...                |

## License

**Web Scraping for Educational Purposes**

This web scraping script is intended for educational purposes only. It demonstrates how to extract data from Amazon's website. Please note that web scraping might be against the terms of service of certain websites. Always ensure you are not violating the website's terms when scraping data.

By using this script, you acknowledge that you are responsible for ensuring that your actions comply with the website's policies and legal requirements.


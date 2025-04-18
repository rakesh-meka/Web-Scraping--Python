# Amazon Headphones Web Scraping

📌 **Project Overview**  
This project is a web scraping application designed to extract headphone product details from Amazon. It scrapes data such as product title, price, reviews, number of reviews, and product image links, then saves the data in a CSV file for further analysis.

![Web Scraping](https://github.com/rakesh-meka/Python_Web_Scraping/blob/main/Web-Scraping--Python.jpg?raw=true)

🎯 **Objectives**  
- **Automate Data Collection** – Efficiently scrape headphone details from Amazon.
- **Flexible Scraping** – Scrape data for a variety of headphone products.
- **Data Storage** – Store the extracted product information in a structured CSV format.
- **Error Handling & Performance** – Implement proper headers and checks to ensure smooth scraping.
- **User-Friendly Experience** – The script runs with minimal configuration required.

🔧 **Technologies & Libraries Used**  
- **Python 3.x**  
- **BeautifulSoup4** – For parsing HTML and extracting product details.  
- **Requests** – For sending HTTP requests to Amazon.  
- **Pandas** – To store and manage scraped data and save it as a CSV file.  
- **LXML** – For fast and efficient HTML parsing.  
- **Regex (Regular Expressions)** – To clean and process data like review counts and prices.

📂 **Features & Workflow**  
1. **User Input** – The scraper fetches data from Amazon's headphone section using a predefined URL.
2. The scraper extracts the following details:
   - **Product Title** 🎧  
   - **Product Price** 💰  
   - **Product Reviews** ⭐  
   - **Number of Reviews** 📝  
   - **Product Image Links** 🌐  
3. **Data Storage** – All the extracted data is saved in a CSV file (e.g., `Headphones_info.csv`) for further analysis.
4. The scraper handles data cleaning, like removing unnecessary terms (e.g., "M.R.P.") and removing trailing numbers.

🚀 **How to Run the Script**  
1. Install the required dependencies:
    ```bash
    pip install beautifulsoup4 requests pandas lxml
    ```
2. Run the script:
    ```bash
    python scrape_headphones.py
    ```
3. The script will scrape data from Amazon and save it to a CSV file in the same directory.

📌 **Example Output (CSV Format)**

| product_title                | product_price | product_reviews   | no_of_reviews | images             |
|------------------------------|---------------|-------------------|---------------|--------------------|
| XYZ Headphone 1               | ₹1,499        | 4.5 out of 5      | 1,200         | `image_url_1.jpg`  |
| XYZ Headphone 2               | ₹2,499        | 4.2 out of 5      | 850           | `image_url_2.jpg`  |
| ...                          | ...           | ...               | ...           | ...                |

⚠️ **Disclaimer**  
This project is intended for **educational purposes only**. Web scraping may violate the terms of service of certain websites. Always ensure that your scraping activities comply with the website's policies and guidelines. This project demonstrates how to extract data from Amazon for learning purposes.

💡 **Happy Scraping! 🚀**

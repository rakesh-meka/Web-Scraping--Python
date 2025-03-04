# 🚲 BikeWale Bikes_info

## 📌 Project Overview  
This **web scraping project** is designed to extract **real-time data** of newly launched bikes from **BikeWale website**. It collects essential information such as:

- **Bike Names**
- **Prices**
- **Launch Dates**
- **Specifications**
- **Image URLs**

The data is then saved in a **CSV file** for further analysis and usage. This script is built and run using **VS Code**.

## 🎯 Objectives  
This project aims to:

- **Automate Data Collection**: Scrape bike details efficiently from BikeWale's new bike launch page.
- **Flexible Scraping**: Scrape information on a variety of newly launched bikes.
- **Data Storage**: Save the scraped data in a **CSV format** for easy analysis and sharing.
- **Error Handling & Performance**: Handle HTTP request issues, and avoid overloading the website.
- **User-Friendly Experience**: Simple to run in VS Code with minimal configuration.

## 🔧 Technologies & Libraries Used  
The following tools and libraries were used for the project:

- **Python 3.x**
- **BeautifulSoup4**: For HTML parsing and data extraction.
- **Requests**: To fetch web pages.
- **Pandas**: To organize the scraped data into a structured CSV file.
- **LXML**: For fast and efficient HTML parsing.

## 📂 Features & Workflow  
1. **User Input**: The scraper will scrape the data from BikeWale’s new bike launches page.
2. **Data Extraction**: The following bike details are collected:
   - **Bike Name** 🏍️
   - **Price** 💰
   - **Launched Date** 📅
   - **Bike Specifications** 🔧
   - **Image URLs** 🖼️
3. **Data Storage**: The scraped data is organized and saved into a **CSV file** for further analysis or use.
4. **Performance Handling**: It handles scraping smoothly without overwhelming the server, ensuring that your requests are human-like.

## 🚀 How to Run the Script  
To run the **BikeWale Scraper** in your **VS Code** setup:

1. **Install the required dependencies**:  
    Open your terminal and run:
    ```bash
    pip install beautifulsoup4 requests pandas lxml
    ```

2. **Run the Python Script**:  
    Open the Python file (e.g., `scrape_bikes.py`) in VS Code and run the script:
    ```bash
    python scrape_bikes.py
    ```

3. **Check the Output**:  
    The script will scrape bike data from the BikeWale website and save it into a file called `Bike_Data.csv` in the same directory.

4. **CSV File**:  
    The script will generate a CSV file with the following structure:
    - **Bike Name**
    - **Price**
    - **Launched Date**
    - **Bike Specifications**
    - **Image URLs**

## ⚠️ Disclaimer  
This project is intended for **educational purposes only**. Web scraping without permission may violate the terms of service of some websites. Always ensure that your scraping activities comply with the website’s **policies**. 

Before deploying or using this scraper extensively, check BikeWale's **scraping policies**.

## 💡 Happy Scraping! 🚀

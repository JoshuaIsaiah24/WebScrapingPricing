# Container Price Scraping & Data Processing Project

This project demonstrates the automation of web scraping using Selenium to extract shipping container prices from a dynamic website, followed by data cleaning and storage using Pandas. The script captures container prices for different ZIP codes, processes the data, and saves it in an Excel file for further analysis.

## Project Overview

The goal of this project is to automate the process of collecting container prices from a dynamic website. We use Selenium to handle the dynamic elements of the webpage, such as entering ZIP codes and navigating between container product pages. The data is then cleaned and processed using Pandas, and the final results are stored in an Excel file.

### Features
- Automated web scraping using Selenium to collect container prices from different ZIP codes.
- Dynamic interaction with website elements (e.g., entering ZIP codes and navigating to product pages).
- Data cleaning and processing using Pandas.
- Export of the cleaned data into an Excel file for further analysis or reporting.

## Tech Stack
- **Python** for writing the scraping script.
- **Selenium** for web scraping from the dynamic website.
- **Pandas** for data processing and cleaning.
- **Excel** for storing the final output.

## Project Workflow

1. **Initialize Web Scraping**:  
   The script starts by initializing the Selenium WebDriver and navigating to the main webpage, which lists the available shipping containers.
   
2. **ZIP Code Input**:  
   For each ZIP code in the provided list, the script enters the ZIP code into the webpage's search box and retrieves product URLs for containers available in that location.

3. **Data Extraction**:  
   For each product URL, the script retrieves key information such as:
   - Container Type
   - Container Price
   - Associated ZIP Code
   
4. **Data Storage**:  
   The collected data is stored in a Pandas DataFrame, which is then exported to an Excel file (`container_prices.xlsx`).

5. **Data Cleaning**:  
   After scraping, the data undergoes basic cleaning steps, such as removing extra spaces and ensuring correct data formatting, before being saved.

### Conclusion

This project successfully demonstrates the power of automating web scraping tasks using Selenium and Python to extract valuable data from dynamic websites. By leveraging Selenium’s capabilities to interact with dynamic web elements and Pandas for data processing, the script effectively gathers and organizes shipping container price information across various ZIP codes.

The resulting data, cleaned and exported into an Excel file, provides a comprehensive view of container pricing trends, which can be crucial for market analysis and business insights. This automation not only streamlines the data collection process but also ensures accuracy and efficiency in handling large volumes of web data.

This approach can be adapted to various other data extraction tasks, making it a versatile tool for anyone needing to interact with dynamic websites and process large datasets. Future improvements could enhance the script’s robustness and expand its functionality, further increasing its utility and impact.

We encourage you to explore the code and adapt it for your specific needs, whether for similar web scraping tasks or other data-driven projects.

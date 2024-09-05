from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from openpyxl import Workbook

# Initialize the WebDriver
driver = webdriver.Chrome()

# Main URL where container types are listed
main_url = "https://www.conexwest.com/shipping-containers-sale"

# List to store data
container_data = []

# ZIP code details
zipcodes = ["07101", "10001", "90001"]

try:
    for zipcode in zipcodes:
        print(f"Attempting to get prices for: {zipcode}")
        # Step 1: Navigate to the main page
        driver.delete_all_cookies()
        driver.get(main_url)
        print("Navigated to the main page.")
        time.sleep(5)  # Wait for the page to load

        # Step 2: Enter the ZIP code
        print("Attempting to enter ZIP code...")
        zipcode_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="edit-zipcode"]'))
        )
        zipcode_input.clear()  # Clear any existing text before entering the new ZIP code
        zipcode_input.send_keys(zipcode)
        zipcode_input.send_keys(Keys.RETURN)
        print(f"Entered ZIP code: {zipcode}")

        # Wait for the ZIP code processing to complete
        time.sleep(5)

        # Step 3: Extract container links
        container_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/shipping-containers-sale/")]'))
        )
        container_urls = [elem.get_attribute('href') for elem in container_elements]
        print(f"Found {len(container_urls)} container URLs for ZIP code {zipcode}.")

        # Step 4: Visit each container page
        for url in container_urls:
            print(f"Processing URL: {url}")
            driver.get(url)
            time.sleep(5)  # Wait for the page to load

            try:
                # Retrieve the container type
                print("Attempting to retrieve container type...")
                type_element = WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="desktop-title"]'))
                )
                container_type = type_element.text.strip()
                print(f"Container Type found: {container_type}")
                
                # Retrieve the price
                print("Attempting to retrieve price...")
                price_element = WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="zipcode-container-price"]'))
                )
                price = price_element.text.strip()
                print(f"Price found: {price}")

                # Collect data
                container_data.append({
                    "URL": url,
                    "Container Type": container_type,
                    "Price": price,
                    "ZIP Code": zipcode
                })
                
            except Exception as e:
                print(f"Could not retrieve data for URL: {url}")
                print(f"Error: {e}")

        # Step 5: Reset ZIP code input for the next iteration
        #try:
            #print("Navigating back to the main page to reset ZIP code...")
            #driver.get(main_url)
            #time.sleep(10) 
            
            #print("Attempting to reset ZIP code input...")
            # Wait for the reset element to be clickable
            #reset_element = WebDriverWait(driver, 30).until(
             #   EC.element_to_be_clickable((By.XPATH, '//div[@class="location-info"]/p[@class="zipcode"]'))
            #)
            #print("Reset element found and clickable.")
            #reset_element.click()
            #print("Reset element clicked.")
            #time.sleep(5)  # Wait for the reset action to complete
        #except Exception as e:
        #    print(f"Error resetting ZIP code input: {e}")


finally:
    # Close the WebDriver
    driver.quit()

# Create a DataFrame from the scraped data
df = pd.DataFrame(container_data)

# Save the DataFrame to an Excel file
df.to_excel("container_prices.xlsx", index=False)

print(df.head())

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import logging

# class InstituteInfoScraper:
#     def __init__(self, url):
#         self.url = url
#         self.setup_logging()

#     def setup_logging(self):
#         logging.basicConfig(
#             level=logging.INFO,
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             filename='scraping.log'
#         )

#     def get_page_content(self):
#         try:
#             # Add headers to mimic a browser request
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#             }
#             response = requests.get(self.url, headers=headers)
#             response.raise_for_status()
#             return response.text
#         except requests.RequestException as e:
#             logging.error(f"Error fetching page: {e}")
#             return None

#     def parse_institute_data(self, html_content):
#         if not html_content:
#             return []

#         soup = BeautifulSoup(html_content, 'html.parser')
#         institutes_data = []
#         print(institutes_data)
#         try:
#             # You'll need to adjust these selectors based on the actual HTML structure
#             institutes = soup.find_all('div', class_='modal-header')  # Adjust this selector
#             print("data\n\n\n\n\n\n\n\n",institutes)
#             for institute in institutes:
#                 institute_info = {
#                     'name': self.safe_extract(institute, 'h2', 'instituteName'),
#                     'city': self.safe_extract(institute, 'div', 'institute-city'),
#                     'state': self.safe_extract(institute, 'div', 'institute-state'),
#                     'contact_name': self.safe_extract(institute, 'div', 'contact-name'),
#                     'phone': self.safe_extract(institute, 'div', 'contact-phone'),
#                     'email': self.safe_extract(institute, 'div', 'contact-email')
#                 }
#                 institutes_data.append(institute_info)

#         except Exception as e:
#             logging.error(f"Error parsing institute data: {e}")

#         return institutes_data

#     def safe_extract(self, element, tag, class_name):
#         """Safely extract text from an HTML element"""
#         try:
#             found = element.find(tag, class_=class_name)
#             return found.text.strip() if found else ''
#         except Exception as e:
#             logging.error(f"Error extracting {class_name}: {e}")
#             return ''

#     def save_to_csv(self, data, filename='institutes_data.csv'):
#         """Save the scraped data to a CSV file"""
#         try:
#             df = pd.DataFrame(data)
#             df.to_csv(filename, index=False)
#             logging.info(f"Data successfully saved to {filename}")
#         except Exception as e:
#             logging.error(f"Error saving to CSV: {e}")

#     def run_scraper(self):
#         logging.info("Starting scraping process")
#         html_content = self.get_page_content()

#         if html_content:
#             institutes_data = self.parse_institute_data(html_content)
#             if institutes_data:
#                 self.save_to_csv(institutes_data)
#                 return True
#         return False

# def main():
#     url = "https://onos.gov.in/instituteList"  # Replace with your target URL
#     scraper = InstituteInfoScraper(url)
#     success = scraper.run_scraper()

#     if success:
#         print("Scraping completed successfully. Check institutes_data.csv for results.")
#     else:
#         print("Scraping failed. Check scraping.log for details.")

# if __name__ == "__main__":
#     main()






# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# class SpecificDataScraper:
#     def __init__(self, url):
#         self.url = url

#     def get_page_content(self):
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#             }
#             response = requests.get(self.url, headers=headers)
#             response.raise_for_status()
#             return response.text
#         except requests.RequestException as e:
#             print(f"Error fetching page: {e}")
#             return None

#     def parse_data(self, html_content):
#         if not html_content:
#             return []

#         soup = BeautifulSoup(html_content, 'html.parser')
#         data = []

#         try:
#             # Locate the modal content
#             modal = soup.find('h2', class_='modal-title fs-5')
#             print(modal,"------------")
#             if modal:
#                 # Extract institute name
#                 name = modal.find('h2', id='instituteName').get_text(strip=True) if modal.find('h2', id='instituteName') else ''
#                 print("name",name)
#                 # Extract contact details
#                 admin_div = modal.find('div', id='adminDiv')
#                 if admin_div:
#                     contact_name = admin_div.find('p', text=lambda t: 'Prof.' in t).get_text(strip=True) if admin_div.find('p') else ''
#                     print("conbatct",contact_name)
#                     phone = admin_div.find('p', text=lambda t: t and '020' in t).get_text(strip=True) if admin_div.find('p') else ''
#                     email = admin_div.find('p', text=lambda t: '@' in t).get_text(strip=True) if admin_div.find('p') else ''

#                     data.append({
#                         'Institute Name': name,
#                         'Contact Name': contact_name,
#                         'Phone': phone,
#                         'Email': email
#                     })

#         except Exception as e:
#             print(f"Error parsing data: {e}")

#         return data

#     def save_to_csv(self, data, filename='institute_data.csv'):
#         try:
#             df = pd.DataFrame(data)
#             df.to_csv(filename, index=False)
#             print(f"Data successfully saved to {filename}")
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")

#     def run(self):
#         html_content = self.get_page_content()
#         if html_content:
#             scraped_data = self.parse_data(html_content)
#             if scraped_data:
#                 self.save_to_csv(scraped_data)
#             else:
#                 print("No data found to scrape.")
#         else:
#             print("Failed to fetch the webpage content.")

# if __name__ == "__main__":
#     # Replace with the actual URL where the data exists
#     url = "https://onos.gov.in/instituteList"  
#     scraper = SpecificDataScraper(url)
#     scraper.run()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import os

# class DynamicDataScraper:
#     def __init__(self, url):
#         self.url = url
#         self.setup_driver()

#     def setup_driver(self):
#         chrome_driver_path = '/home/manish/.wdm/drivers/chromedriver/linux64/131.0.6778.264/chromedriver-linux64/chromedriver'  # Update with your `chromedriver` path
#         chrome_options = Options()
#         # chrome_options.add_argument("--headless")  # Run in headless mode
#         # chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         if not os.path.exists(chrome_driver_path):
#             raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")
#         self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

#     def get_dynamic_content(self):
#         try:
#             self.driver.get(self.url)
#             time.sleep(5)  # Allow time for dynamic content to load
#             return self.driver.page_source
#         except Exception as e:
#             print(f"Error fetching dynamic content: {e}")
#             return None

#     def parse_data(self, html_content):
#         if not html_content:
#             return []

#         soup = BeautifulSoup(html_content, 'html.parser')
#         data = []

#         try:
#             # Locate the table
#             table = soup.find('table', class_="display dataTable")
#             if table:
#                 # Extract column headers from the table's thead
#                 header_row = table.find('thead').find('tr')
#                 headers = [th.find('span', class_='dt-column-title').get_text(strip=True) for th in header_row.find_all('th') if th.find('span', class_='dt-column-title')]

#                 print("Extracted Headers:", headers)

#                 # (Optional) Extract table data from tbody if present
#                 rows = table.find('tbody').find_all('tr')
#                 for row in rows:
#                     cells = row.find_all('td')
#                     row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
#                     data.append(row_data)

#             print("\nExtracted Data:\n", data)

#         except Exception as e:
#             print(f"Error parsing data: {e}")

#         return data


#     def save_to_csv(self, data, filename='institute_data.csv'):
#         try:
#             df = pd.DataFrame(data)
#             df.to_csv(filename, index=False)
#             print(f"Data successfully saved to {filename}")
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")

#     def run(self):
#         html_content = self.get_dynamic_content()
#         if html_content:
#             scraped_data = self.parse_data(html_content)
#             if scraped_data:
#                 self.save_to_csv(scraped_data)
#             else:
#                 print("No data found to scrape.")
#         else:
#             print("Failed to fetch the webpage content.")
#         self.driver.quit()

# if __name__ == "__main__":
#     # Replace with the actual URL where the data exists
#     url = "https://onos.gov.in/instituteList"  
#     scraper = DynamicDataScraper(url)
#     scraper.run()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import os

# class DynamicDataScraper:
#     def __init__(self, url):
#         self.url = url
#         self.setup_driver()

#     def setup_driver(self):
#         chrome_driver_path = '/home/manish/.wdm/drivers/chromedriver/linux64/131.0.6778.264/chromedriver-linux64/chromedriver'  # Update with your `chromedriver` path
#         chrome_options = Options()
#         # chrome_options.add_argument("--headless")  # Run in headless mode
#         # chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         if not os.path.exists(chrome_driver_path):
#             raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")
#         self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

#     def get_dynamic_content(self):
#         try:
#             self.driver.get(self.url)
#             time.sleep(5)  # Allow time for dynamic content to load
#             return self.driver.page_source
#         except Exception as e:
#             print(f"Error fetching dynamic content: {e}")
#             return None

#     def parse_data(self, html_content):
#         if not html_content:
#             return []

#         soup = BeautifulSoup(html_content, 'html.parser')
#         data = []

#         try:
#             # Locate the table
#             table = soup.find('table', class_="display dataTable")
#             if table:
#                 # Extract column headers from the table's thead
#                 header_row = table.find('thead').find('tr')
#                 headers = [th.find('span', class_='dt-column-title').get_text(strip=True) for th in header_row.find_all('th') if th.find('span', class_='dt-column-title')]

#                 # Extract table data from tbody if present
#                 rows = table.find('tbody').find_all('tr')
#                 for row in rows:
#                     cells = row.find_all('td')
#                     row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
#                     data.append(row_data)

#         except Exception as e:
#             print(f"Error parsing data: {e}")

#         return data

#     def scrape_all_pages(self):
#         all_data = []
#         try:
#             current_page = 1
#             while True:
#                 print(f"Scraping page {current_page}...")
#                 html_content = self.get_dynamic_content()
#                 page_data = self.parse_data(html_content)
#                 if page_data:
#                     all_data.extend(page_data)

#                 # Locate the "Next" button and click if available
#                 try:
#                     next_button = self.driver.find_element(By.CSS_SELECTOR, 'button.dt-paging-button.next')
#                     if next_button.is_enabled():
#                         next_button.click()
#                         time.sleep(3)  # Wait for the next page to load
#                         current_page += 1
#                     else:
#                         print("No more pages to scrape.")
#                         break
#                 except Exception as e:
#                     print(f"No 'Next' button found or end of pagination: {e}")
#                     break

#         except Exception as e:
#             print(f"Error during pagination: {e}")
#         return all_data


#     def save_to_csv(self, data, filename='institute_data.csv'):
#         try:
#             df = pd.DataFrame(data)
#             df.to_csv(filename, index=False)
#             print(f"Data successfully saved to {filename}")
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")

#     def run(self):
#         try:
#             all_data = self.scrape_all_pages()
#             if all_data:
#                 self.save_to_csv(all_data)
#             else:
#                 print("No data found to scrape.")
#         finally:
#             self.driver.quit()

# if __name__ == "__main__":
#     # Replace with the actual URL where the data exists
#     url = "https://onos.gov.in/instituteList"  
#     scraper = DynamicDataScraper(url)
#     scraper.run()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import pandas as pd
# import os

# class DynamicDataScraper:
#     def __init__(self, url):
#         self.url = url
#         self.setup_driver()

#     def setup_driver(self):
#         chrome_driver_path = '/home/manish/.wdm/drivers/chromedriver/linux64/131.0.6778.264/chromedriver-linux64/chromedriver'
#         chrome_options = Options()
#         # chrome_options.add_argument("--headless")  # Uncomment for headless mode
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         if not os.path.exists(chrome_driver_path):
#             raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")
#         self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

#     def parse_data(self, html_content):
#         soup = BeautifulSoup(html_content, 'html.parser')
#         data = []

#         try:
#             table = soup.find('table', class_="display dataTable")
#             print("\n\n\n",table,"\n\n\n")
#             if table:
#                 headers = [th.find('span', class_='dt-column-title').get_text(strip=True) for th in table.find('thead').find_all('th') if th.find('span', class_='dt-column-title')]
#                 rows = table.find('tbody').find_all('tr')

                
#                 for row in rows:
#                     # Extract cell data
#                     cells = row.find_all('td')
#                     view_buttons = row.find_all("button")  # Find all buttons in the row
                    
#                     # Initialize row data with cell information
#                     row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}

#                     for button in view_buttons:
#                         button_id = button.get('class')  # Example: ID to identify the button
#                         print(f"Processing button with ID: {button_id}")

#                         try:
#                             # Find and click the button using Selenium
#                             button_element = self.driver.find_element(By.ID, button_id)
#                             button_element.click()

#                             # Wait for modal content to appear
#                             WebDriverWait(self.driver, 10).until(
#                                 EC.presence_of_element_located((By.ID, 'adminDiv'))
#                             )

#                             # Extract modal content
#                             modal_html = self.driver.find_element(By.ID, 'adminDiv').get_attribute('outerHTML')
#                             modal_soup = BeautifulSoup(modal_html, 'html.parser')

#                             # Parse details from `adminDiv`
#                             admin_details = {}
#                             library_contact = modal_soup.find('strong', class_='d-inline-block').get_text(strip=True)
#                             admin_details['Library Contact'] = library_contact

#                             # Extract specific fields
#                             contact_info = modal_soup.find_all('p', class_='card-text')
#                             for info in contact_info:
#                                 text = info.get_text(strip=True)
#                                 if "Prof." in text:  # Example: Check if it's a name
#                                     admin_details['Name'] = text
#                                 elif "@" in text:  # Check if it's an email
#                                     admin_details['Email'] = text
#                                 elif text.isdigit():  # Check if it's a phone number
#                                     admin_details['Phone'] = text

#                             # Add parsed modal data to row_data
#                             row_data.update(admin_details)

#                             # Close the modal
#                             close_button = self.driver.find_element(By.CSS_SELECTOR, 'button.btn-close')
#                             close_button.click()

#                             # Wait for modal to disappear
#                             WebDriverWait(self.driver, 10).until(
#                                 EC.invisibility_of_element_located((By.ID, 'adminDiv'))
#                             )

#                         except Exception as e:
#                             print(f"Error processing button ID {button_id}: {e}")

#                     # Append the row's data to the main dataset
#                     data.append(row_data)

#         except Exception as e:
#             print(f"Error parsing data: {e}")

#         # return data

#     def scrape_all_pages(self):
#         all_data = []
#         current_page = 1

#         try:
#             self.driver.get(self.url)
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'table.display.dataTable'))
#             )

#             while True:
#                 print(f"Scraping page {current_page}...")
#                 html_content = self.driver.page_source
#                 page_data = self.parse_data(html_content)
#                 if page_data:
#                     all_data.extend(page_data)
#                 else:
#                     print("No data found on this page. Stopping.")
#                     break

#                 try:
#                     next_button = WebDriverWait(self.driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dt-paging-button.next'))
#                     )

#                     # Click the "Next" button
#                     self.driver.execute_script("arguments[0].scrollIntoView();", next_button)
#                     next_button.click()
#                     WebDriverWait(self.driver, 10).until(
#                         EC.staleness_of(next_button)
#                     )  # Wait for the page to reload
#                     current_page += 1

#                 except Exception as e:
#                     print(f"No 'Next' button found or unable to navigate further: {e}")
#                     break

#         except Exception as e:
#             print(f"Error during scraping: {e}")
#         # return all_data

#     def save_to_csv(self, data, filename='institute_data.csv'):
#         try:
#             df = pd.DataFrame(data)
#             df.to_csv(filename, index=False)
#             print(f"Data successfully saved to {filename}")
#         except Exception as e:
#             print(f"Error saving to CSV: {e}")

#     def run(self):
#         try:
#             all_data = self.scrape_all_pages()
#             if all_data:
#                 self.save_to_csv(all_data)
#             else:
#                 print("No data found to scrape.")
#         finally:
#             self.driver.quit()

# if __name__ == "__main__":
#     url = "https://onos.gov.in/instituteList"
#     scraper = DynamicDataScraper(url)
#     scraper.run()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os


class DynamicDataScraper:
    def __init__(self, url):
        self.url = url
        self.setup_driver()

    def setup_driver(self):
        chrome_driver_path = '/usr/bin/chromedriver'
        chrome_options = Options()
        # Uncomment the next line to enable headless mode
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        if not os.path.exists(chrome_driver_path):
            raise FileNotFoundError(f"ChromeDriver not found at {chrome_driver_path}")
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    def parse_table(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data = []

        try:
            table = soup.find('table', class_="display dataTable")
            if table:
                headers = [
                    th.find('span', class_='dt-column-title').get_text(strip=True) 
                    for th in table.find('thead').find_all('th') 
                    if th.find('span', class_='dt-column-title')
                ]
                rows = table.find('tbody').find_all('tr')

                for row in rows:
                    cells = row.find_all('td')
                    row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
                    data.append(row_data)
        except Exception as e:
            print(f"Error parsing table data: {e}")

        return data

    def extract_modal_data(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.view-details')
        modal_data = []

        for button_index, button in enumerate(buttons):
            try:
                # Scroll to the button and click
                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                button.click()

                # Wait for the modal to open
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.modal.show'))
                )

                # Extract modal content
                modal_element = self.driver.find_element(By.CSS_SELECTOR, '.modal.show')
                modal_html = modal_element.get_attribute('innerHTML')
                modal_soup = BeautifulSoup(modal_html, 'html.parser')

                # Parse modal content
                modal_content = {}

                # Extract Institute Name
                institute_name_tag = modal_soup.find('h2', class_='modal-title')
                if institute_name_tag:
                    modal_content['Institute Name'] = institute_name_tag.get_text(strip=True)

                # Extract Library Contact Details
                admin_div = modal_soup.find('div', id='adminDiv')
                if admin_div:
                    contact_details = {}
                    # Name
                    name_tag = admin_div.find('svg', {'data-icon': 'user'})
                    if name_tag:
                        contact_details['Name'] = name_tag.find_next('p').get_text(strip=True)
                    # Phone
                    phone_tag = admin_div.find('svg', {'data-icon': 'phone'})
                    if phone_tag:
                        contact_details['Phone'] = phone_tag.find_next('p').get_text(strip=True)
                    # Email
                    email_tag = admin_div.find('svg', {'data-icon': 'envelope'})
                    if email_tag:
                        contact_details['Email'] = email_tag.find_next('p').get_text(strip=True)

                    modal_content['Library Contact Details'] = contact_details

                # Extract Technical Details (if any)
                technical_div = modal_soup.find('div', id='technicalDiv')
                if technical_div:
                    modal_content['Technical Details'] = technical_div.get_text(strip=True)

                # Add modal content to list
                modal_data.append(modal_content)

                # Close the modal
                close_button = modal_element.find_element(By.CSS_SELECTOR, '.btn-close')
                close_button.click()

                # Wait for the modal to close
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal.show'))
                )

            except Exception as e:
                print(f"Error processing button {button_index + 1}: {e}")
                # Ensure modal is closed in case of errors
                try:
                    close_button = self.driver.find_element(By.CSS_SELECTOR, '.modal.show .btn-close')
                    close_button.click()
                    WebDriverWait(self.driver, 10).until(
                        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal.show'))
                    )
                except Exception as close_error:
                    print(f"Error closing modal: {close_error}")

        return modal_data


    def scrape_all_pages(self):
        all_table_data = []
        all_modal_data = []
        current_page = 1

        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'table.display.dataTable'))
            )

            while True:
                print(f"Scraping page {current_page}...")

                # Parse table data
                table_data = self.parse_table()
                if table_data:
                    all_table_data.extend(table_data)

                # Extract modal data
                modal_data = self.extract_modal_data()
                if modal_data:
                    all_modal_data.extend(modal_data)

                # Attempt to go to the next page
                try:
                    next_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dt-paging-button.next'))
                    )
                    next_button.click()
                    WebDriverWait(self.driver, 10).until(
                        EC.staleness_of(next_button)
                    )
                    current_page += 1
                except Exception as e:
                    print(f"No 'Next' button found or unable to navigate further: {e}")
                    break

        except Exception as e:
            print(f"Error during scraping: {e}")

        return all_table_data, all_modal_data

    def save_to_csv(self, data, filename):
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def run(self):
        try:
            table_data, modal_data = self.scrape_all_pages()

            if table_data:
                self.save_to_csv(table_data, 'table_data.csv')
            else:
                print("No table data found.")

            if modal_data:
                self.save_to_csv(modal_data, 'modal_data.csv')
            else:
                print("No modal data found.")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://onos.gov.in/instituteList"  # Replace with the actual URL
    scraper = DynamicDataScraper(url)
    scraper.run()

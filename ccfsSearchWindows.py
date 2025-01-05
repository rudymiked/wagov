import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

class Business:
    def __init__(self, name, ubi, business_type, address, agent_name, status):
        self.name = name
        self.ubi = ubi
        self.business_type = business_type
        self.address = address
        self.agent_name = agent_name
        self.status = status

    def __repr__(self):
        return f"Business(name={self.name}, ubi={self.ubi}, business_type={self.business_type}, address={self.address}, agent_name={self.agent_name}, status={self.status})"

def start_search():
    keywords = entry.get().split(',')
    keywords = [keyword.strip() for keyword in keywords]

    # Initialize the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    # Open the website
    driver.get("https://ccfs.sos.wa.gov/?_gl=1*wq7u93*_ga*MTA2NzA5NzA2LjE3MzYwNTA1NjI.*_ga_7B08VE04WV*MTczNjA1MDU2MS4xLjEuMTczNjA1MDY3Mi4wLjAuMA..#/AdvancedSearch")

    # Wait for the page to load
    # Wait for the page to load by checking for the presence of a specific element

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlSelection"))
    )

    # List to store results
    businesses = []

    for keyword in keywords:
        # Fill in the search form
        search_type = driver.find_element(By.ID, "ddlSelection")
        search_type.send_keys("Contains")

        business_name = driver.find_element(By.ID, "txtOrgname")
        business_name.clear()  # Clear the input field before entering new keyword
        business_name.send_keys(keyword)

        start_date = driver.find_element(By.ID, "txtStartDateOfIncorporation")
        start_date.clear()  # Clear the input field before entering new date
        # Ensure the date is in the format dd/mm/yyyy
        raw_date = start_date_entry.get()

        try:
            parsed_date = time.strptime(raw_date, "%d/%m/%Y")
            formatted_date = time.strftime("%d/%m/%Y", parsed_date)
        except ValueError:
            try:
                parsed_date = time.strptime(raw_date, "%d/%m/%y")
                formatted_date = time.strftime("%d/%m/%Y", parsed_date)
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter a valid date in the format dd/mm/yyyy or dd/mm/yy.")
                return

        start_date.send_keys(formatted_date)

        # Click the "Search" button
        search_button = driver.find_element(By.ID, "btnSearch")
        search_button.click()

        # Wait for the results to load
        time.sleep(5)  # Increase wait time to ensure the page is fully loaded

        # Save screenshot for each keyword
        # driver.save_screenshot(f"ccfsSearchResults_{keyword}.png")

        html_content = driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table containing the business data
        table = soup.find('table', {'class': 'table table-striped table-responsive'})

        if table:
            # Iterate over the rows of the table (excluding the header row)
            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')
                if len(cells) >= 6:
                    name = cells[0].text.strip() if cells[0].text.strip() else "N/A"
                    ubi = cells[1].text.strip() if cells[1].text.strip() else "N/A"
                    business_type = cells[2].text.strip() if cells[2].text.strip() else "N/A"
                    address = cells[3].text.strip() if cells[3].text.strip() else "N/A"
                    agent_name = cells[4].text.strip() if cells[4].text.strip() else "N/A"
                    status = cells[5].text.strip() if cells[5].text.strip() else "N/A"
                    business = Business(name, ubi, business_type, address, agent_name, status)
                    businesses.append(business)
                    print(f"Added business: {business}")  # Debug print
        else:
            print(f"No table found for keyword: {keyword}")

        # Go back to the search page for the next keyword
        driver.get("https://ccfs.sos.wa.gov/?_gl=1*wq7u93*_ga*MTA2NzA5NzA2LjE3MzYwNTA1NjI.*_ga_7B08VE04WV*MTczNjA1MDU2MS4xLjEuMTczNjA1MDY3Mi4wLjAuMA..#/AdvancedSearch")
        time.sleep(3)

    # Close the browser
    driver.quit()

    # Save results to a CSV file
    with open("ccfsSearchResults.csv", "w", newline='') as csvfile:
        fieldnames = ['name', 'ubi', 'business_type', 'address', 'agent_name', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for business in businesses:
            writer.writerow({
                'name': business.name,
                'ubi': business.ubi,
                'business_type': business.business_type,
                'address': business.address,
                'agent_name': business.agent_name,
                'status': business.status
            })

    # Show a message box with the results
    messagebox.showinfo("Search Complete", f"Search complete. {len(businesses)} businesses found.\nInformation saved here: ccfsSearchResults.csv")

def update_spinner():
    while searching:
        for char in "|/-\\":
            spinner_label.config(text=char)
            time.sleep(0.1)
            root.update_idletasks()

def start_search_with_spinner():
    global searching
    searching = True
    start_button.config(state=tk.DISABLED)  # Disable the start button
    spinner_thread = threading.Thread(target=update_spinner)
    spinner_thread.start()
    search_thread = threading.Thread(target=run_search)
    search_thread.start()

def run_search():
    start_search()
    global searching
    searching = False
    spinner_label.config(text="")
    start_button.config(state=tk.NORMAL)  # Enable the start button

def close_app():
    root.destroy()

###### UI CODE ######

# Create the main window
root = tk.Tk()
root.title("CCFS Search")

# Create and place the widgets
label = tk.Label(root, text="Keywords (separated by commas):")
label.pack(pady=10, padx=20)

searching = False
entry = tk.Entry(root, width=50)
entry.pack(pady=10, padx=20)

start_date_label = tk.Label(root, text="Start date (MM/DD/YYYY):")
start_date_label.pack(pady=10, padx=20)
start_date_label.pack(pady=10)

start_date_entry = tk.Entry(root, width=50)
start_date_entry.pack(pady=10, padx=20)

spinner_label = tk.Label(root, text="", font=("Helvetica", 16))
spinner_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_search_with_spinner)
start_button.pack(side=tk.LEFT, padx=5)

close_button = tk.Button(button_frame, text="Close", command=close_app)
close_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
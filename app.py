import csv
from lxml import html
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

class Business:
    def __init__(self, name, ubi, business_type, address, agent_name, status, ein):
        self.name = name
        self.ubi = ubi
        self.business_type = business_type
        self.address = address
        self.agent_name = agent_name
        self.status = status
        self.ein = ein

    def __repr__(self):
        return f"Business(name={self.name}, ubi={self.ubi}, business_type={self.business_type}, address={self.address}, agent_name={self.agent_name}, status={self.status})"

businesses = []
h3_text = ""
csv_filename = ""

def fetch_data():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9230')
    
    # Correct usage of EdgeDriver
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=options)

    try:
        driver.get("https://ccfs.sos.wa.gov/?_gl=1*wq7u93*_ga=MTA2NzA5NzA2LjE3MzYwNTA1NjI.*_ga_7B08VE04WV=MTczNjA1MDU2MS4xLjEuMTczNjA1MDY3Mi4wLjAuMA..#/AdvancedSearch")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))

        html_content = driver.page_source
        tree = html.fromstring(html_content)

        # Extract the <h3> text
        h3_element = tree.xpath('//h3')
        h3_text = h3_element[0].text.strip() if h3_element else "No Title Found"
        print(f"h3_text: {h3_text}")

    except Exception as e:
        print(f"An error occurred: {e}")
        h3_text = "Error occurred"
    finally:
        driver.quit()

    return h3_text

def start_search(keywords, start_date):
    global businesses

    # Clear the businesses list before starting
    businesses = []

    # Set up a directory for downloaded files
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    for keyword in keywords:
        # Configure WebDriver options for file download
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--remote-debugging-port=9230')
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)

        # Create a new WebDriver instance
        service = EdgeService()
        driver = webdriver.Edge(service=service, options=options)

        try:
            print(f"Searching for keyword: {keyword}")
            driver.get("https://ccfs.sos.wa.gov/?_gl=1*wq7u93*_ga=MTA2NzA5NzA2LjE3MzYwNTA1NjI.*_ga_7B08VE04WV=MTczNjA1MDU2MS4xLjEuMTczNjA1MDY3Mi4wLjAuMA..#/AdvancedSearch")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlSelection")))

            # Set search parameters
            search_type = driver.find_element(By.ID, "ddlSelection")
            search_type.send_keys("Contains")

            business_name = driver.find_element(By.ID, "txtOrgname")
            business_name.clear()
            business_name.send_keys(keyword)

            start_date_field = driver.find_element(By.ID, "txtStartDateOfIncorporation")
            start_date_field.clear()
            start_date_field.send_keys(start_date)

            # Click the search button
            search_button = driver.find_element(By.ID, "btnSearch")
            search_button.click()

            # Wait for the results to load
            WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.CSS_SELECTOR, "table.table-striped tbody tr:not(.ng-hide)")
            )

            # Locate and click the "Export to CSV" button
            export_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@title="Export to CSV"]'))
            )
            export_button.click()

            # Wait for the file to be downloaded
            WebDriverWait(driver, 20).until(
                lambda d: any(fname.endswith(".csv") for fname in os.listdir(download_dir))
            )

            # Find the downloaded CSV file
            csv_file = next(
                (os.path.join(download_dir, fname) for fname in os.listdir(download_dir) if fname.endswith(".csv")),
                None
            )

            if csv_file:
                # Read and parse the CSV file
                with open(csv_file, "r", newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        business = Business(
                            name=row.get("Business Name", "N/A"),
                            ubi=row.get("UBI#", "N/A"),
                            business_type=row.get("Business Type", "N/A"),
                            address=row.get("Principal Office Address", "N/A"),
                            agent_name=row.get("Registered Agent Name", "N/A"),
                            status=row.get("Status", "N/A"),
                            ein=row.get("Nonprofit EIN", "N/A"),
                        )
                        businesses.append(business)
                        print(f"Added business: {business}")

                # Remove the CSV file after processing
                os.remove(csv_file)

        except Exception as e:
            print(f"An error occurred while processing keyword '{keyword}': {e}")
        finally:
            driver.quit()

    return businesses

@app.route('/', methods=['GET', 'POST'])
def index():
    global businesses, csv_filename
    last_modified_time = datetime.fromtimestamp(os.path.getmtime(__file__)).strftime('%Y-%m-%d %H:%M:%S')

    # Generate a unique filename with a timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    csv_filename = f"ccfsSearchResults_{timestamp}.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)

    if request.method == 'POST':
        keywords = request.form['keywords']
        start_date = request.form['start_date']
        if not keywords or not start_date:
            flash('Please enter both keywords and start date.')
            return redirect(url_for('index'))
        try:
            print(f'Keywords: {keywords}')
            print(f'Start Date: {start_date}')
            businesses.clear()
            businesses = start_search([keyword.strip() for keyword in keywords.split(',')], start_date)
            print(f'Businesses: {businesses}')
            
            with open(csv_filepath, "w", newline='') as csvfile:
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
                        'status': business.status,
                        "ein": business.ein
                    })

            flash('Search complete. Results are displayed below.')
            return render_template('index.html', last_modified_time=last_modified_time, title="Search Results", businesses=businesses, csv_filename=csv_filename)
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            flash(f'An error occurred: {str(e)}')
        return redirect(url_for('index'))
    else:
        h3_text = fetch_data()
    
    # Get the last modified time of the app.py file
    return render_template('index.html', last_modified_time=last_modified_time, title=h3_text, businesses=businesses,csv_filename=csv_filename)

@app.route('/results')
def results():
    global businesses, csv_filename
    return jsonify({
        'businesses': [business.__dict__ for business in businesses],
        'csv_filename': csv_filename
    })

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

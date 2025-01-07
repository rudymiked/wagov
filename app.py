from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv
import os
import concurrent.futures

app = Flask(__name__, template_folder='.')
app.secret_key = 'your_secret_key'

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

businesses = []

def fetch_data(keyword, start_date):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://ccfs.sos.wa.gov/?_gl=1*wq7u93*_ga=MTA2NzA5NzA2LjE3MzYwNTA1NjI.*_ga_7B08VE04WV=MTczNjA1MDU2MS4xLjEuMTczNjA1MDY3Mi4wLjAuMA..#/AdvancedSearch")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlSelection")))

        search_type = driver.find_element(By.ID, "ddlSelection")
        search_type.send_keys("Contains")

        business_name = driver.find_element(By.ID, "txtOrgname")
        business_name.clear()
        business_name.send_keys(keyword)

        start_date_field = driver.find_element(By.ID, "txtStartDateOfIncorporation")
        start_date_field.clear()
        start_date_field.send_keys(start_date)

        search_button = driver.find_element(By.ID, "btnSearch")
        search_button.click()

        time.sleep(4)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table', {'class': 'table table-striped table-responsive'})

        if table:
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
                    print(f"Added business: {business}")
    finally:
        driver.quit()

def start_search(keywords, start_date):
    global businesses
    businesses = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_data, keyword, start_date) for keyword in keywords]
        concurrent.futures.wait(futures)

    csv_filename = "ccfsSearchResults.csv"
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
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
                'status': business.status
            })

    return csv_filepath

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keywords = request.form['keywords']
        start_date = request.form['start_date']
        if not keywords or not start_date:
            flash('Please enter both keywords and start date.')
            return redirect(url_for('index'))
        try:
            csv_filepath = start_search(keywords.split(','), start_date)
            flash('Search complete. Results are displayed below.')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
        return redirect(url_for('index'))
    
    # Get the last modified time of the app.py file
    last_modified_time = datetime.fromtimestamp(os.path.getmtime(__file__)).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', last_modified_time=last_modified_time)

@app.route('/results')
def results():
    global businesses
    return jsonify([business.__dict__ for business in businesses])

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
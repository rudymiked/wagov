import csv
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from datetime import datetime
import requests
import os
import time

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
h3_text = "Corporations and Charities Filing System"
csv_filename = ""

def start_search(keywords, start_date):
    global businesses

    # Clear the businesses list before starting
    businesses = []

    # API endpoint
    api_url = "https://ccfs-api.prod.sos.wa.gov/api/BusinessSearch/GetAdvanceBusinessSearchList"

    principal_headers = {
        'Accept-Language': 'en-US,en;q=0.8,es-AR;q=0.5,es;q=0.3',
        'Referer': 'https://ccfs.sos.wa.gov/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Origin': 'https://ccfs.sos.wa.gov'
    }

    for keyword in keywords:
        print(f"Fetching data for keyword: {keyword}")

        # Payload for the POST request
        payload = {
            "Type": "Agent",
            "BusinessStatusID": 0,
            "SearchEntityName": f"%{keyword}%",
            "SearchType": "Contains",
            "BusinessTypeID": 0,
            "AgentName": "",
            "PrincipalName": "",
            "StartDateOfIncorporation": start_date,
            "EndDateOfIncorporation": "",
            "ExpirationDate": "",
            "IsSearch": True,
            "IsShowAdvanceSearch": True,
            "AgentAddress[IsAddressSame]": False,
            "AgentAddress[IsValidAddress]": False,
            "AgentAddress[isUserNonCommercialRegisteredAgent]": False,
            "AgentAddress[IsInvalidState]": False,
            "AgentAddress[FullAddress]": ", WA, USA",
            "AgentAddress[State]": "WA",
            "AgentAddress[Country]": "USA",
            "PrincipalAddress[IsAddressSame]": False,
            "PrincipalAddress[IsValidAddress]": False,
            "PrincipalAddress[isUserNonCommercialRegisteredAgent]": False,
            "PrincipalAddress[IsInvalidState]": False,
            "PrincipalAddress[FullAddress]": ", WA, USA",
            "PrincipalAddress[State]": "",
            "PrincipalAddress[Country]": "USA",
            "PageID": 1,
            "PageCount": 25,
        }

        # Log the request details
        print("POST Request Details:")
        print(f"URL: {api_url}")
        print(f"Headers: {principal_headers}")
        print(f"Payload: {payload}")

        # Send the POST request
        response = requests.post(api_url, data=payload, headers=principal_headers)

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            for item in data:
                business = Business(
                    name=item.get("BusinessName", "N/A"),
                    ubi=item.get("UBINumber", "N/A"),
                    business_type=item.get("BusinessType", "N/A"),
                    address=item.get("FullAddress", "N/A"),
                    agent_name=item.get("AgentName", "N/A"),
                    status=item.get("BusinessStatus", "N/A"),
                    ein=item.get("BusinessID", "N/A"),
                )
                businesses.append(business)
                print(f"Added business: {business}")
        elif response.status_code == 429:
            # Handle rate-limiting
            retry_after = int(response.headers.get("Retry-After", 1))  # Default to 1 second if not provided
            print(f"Rate limit hit. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
        else:
            print(f"Failed to fetch data for keyword '{keyword}'. Status code: {response.status_code}")

        # Add a delay to avoid hitting the rate limit
        time.sleep(1)  # Adjust the delay as needed (e.g., 1 second)

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
                fieldnames = ['name', 'ubi', 'business_type', 'address', 'agent_name', 'status', 'ein']
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
                        'ein': business.ein
                    })

            flash('Search complete. Results are displayed below.')
            return render_template('index.html', last_modified_time=last_modified_time, title="Search Results", businesses=businesses, csv_filename=csv_filename)
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            flash(f'An error occurred: {str(e)}')
        return redirect(url_for('index'))
    else:
        h3_text = "Corporations and Charities Filing System"
    
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

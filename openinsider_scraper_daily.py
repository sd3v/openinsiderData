import csv
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

# Set up logging once, instead of in every function call
logging.basicConfig(filename='logs.txt', level=logging.WARNING)
logger = logging.getLogger()

def get_data_for_date(date):
    # Create a string in the format MM/DD/YYYY
    date_string = date.strftime('%m/%d/%Y')

    # Combine the start and end date strings into one URL string
    url_date_range = f"{date_string}+-+{date_string}"

    # Initialize an empty set to store the data for the date
    data = set()

    # Make a request to the website
    url = f'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=-1&fdr={url_date_range}&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=5000&page=1'
    response = requests.get(url)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    tinytable = soup.find('table', {'class': 'tinytable'})

    if tinytable is None
        print(f"No data for {date_string}")
    return data

    # Find all the rows in the table on the website
    rows = tinytable.find('tbody').findAll('tr', recursive=False)

    # Loop through each row and extract the insider transaction data
    for row in rows:
        cells = row.findAll('td', recursive=False)
        if not cells:
            continue
        data.add(tuple(cell.text.strip() for cell in cells))

    return data

def get_openinsider_data():
    # go through all dates
    with ThreadPoolExecutor(max_workers=10) as executor:
        all_data = []
        start_date = datetime(2013, 1, 1)
        end_date = datetime.now()
        date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

        # iterate through all dates
        for date in date_range:
            # get data for date with multi-threading
            futures = [executor.submit(get_data_for_date, date)]
            for future in futures:
                all_data.extend(future.result())
            print(f"finished retrieving {date}")

        # set field names for CSV file
        field_names = ['transaction_date','trade_date', 'ticker', 'company_name', 'owner_name', 'Title' ,'transaction_type', 'last_price', 'Qty', 'shares_held', 'Owned', 'Value']

        # Open a CSV file for writing
        with open('output_all_dates_daily.csv', 'w', newline='') as f:
            writer = csv.writer(f)

            # Write the column names in the first line of the CSV file
            writer.writerow(field_names)

            # Write the values of each transaction to the CSV file
            for transaction in all_data:
                writer.writerow(transaction)

# execute the function
get_openinsider_data()

import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor
import logging
from datetime import datetime, timedelta
from sys import exit

def get_data_for_month(year, month):
    # Create a logger instance with the name "my_logger"
    my_logger = logging.getLogger("my_logger")

    # Set the log level to INFO (other options: WARNING, ERROR, etc.)
    my_logger.setLevel(logging.WARNING)

    # Create a FileHandler to write the messages to a file
    file_handler = logging.FileHandler("logs.txt")

    # Set the log level for the FileHandler to INFO
    file_handler.setLevel(logging.WARNING)

    # Add the FileHandler to the logger instance
    my_logger.addHandler(file_handler)

    # Set the start date and end date for the given month
    start_date = datetime(year, month, 1).strftime('%m/%d/%Y')
    end_date = (datetime(year, month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    end_date = end_date.strftime('%m/%d/%Y')

    # Print which month is currently being processed
    print(f"processing month: {month}-{year}")

    # Initialize an empty set to store the data for the month
    data = set()

    # Make a request to the website
    url = f'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=-1&fdr={start_date}+-+{end_date}&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=5000&page=1'
    response = requests.get(url)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the rows in the table on the website
    try:
        rows = soup.find('table', {'class': 'tinytable'}).find('tbody').findAll('tr')
    except:
        print("Error! Skipping")
          # If there is an error, log which URL failed for further research and skip to the next page
        my_logger.error("This URL was not successful: {}".format(url))
        return
    
    # Loop through each row and extract the insider transaction data
    for row in rows:
        if not row.findAll('td'):
            continue
        insider_data = {}
        insider_data['transaction_date'] = row.findAll('td')[1].find('a').text.strip()
        insider_data['trade_date'] = row.findAll('td')[2].text.strip()
        insider_data['ticker'] = row.findAll('td')[3].find('a').text.strip()
        insider_data['company_name'] = row.findAll('td')[4].find('a').text.strip()
        insider_data['owner_name'] = row.findAll('td')[5].find('a').text.strip()
        insider_data['Title'] = row.findAll('td')[6].text.strip()
        insider_data['transaction_type'] = row.findAll('td')[7].text.strip()
        insider_data['last_price'] = row.findAll('td')[8].text.strip()
        insider_data['Qty'] = row.findAll('td')[9].text.strip()
        insider_data['shares_held'] = row.findAll('td')[10].text.strip()
        insider_data['Owned'] = row.findAll('td')[11].text.strip()
        insider_data['Value'] = row.findAll('td')[12].text.strip()
        # Add the Data to the Stack
        data.add(tuple(insider_data.values()))
    return data

def get_openinsider_data():

    # go through all dates
    with ThreadPoolExecutor(max_workers=10) as executor:
        all_data = []
        current_year = datetime.now().year
        current_month = datetime.now().month
         # iterate through years and months
        for year in range(2013, current_year + 1):
            start_month = 1
            end_month = 12
            # set start and end month for first and last year
            if year == 2013:
                start_month = 3
            if year == current_year:
                end_month = current_month
            for month in range(start_month, end_month + 1):
                # get data for month with multi-threading
                futures = [executor.submit(get_data_for_month, year, month)]
                for future in futures:
                    all_data.extend(future.result())
                print(f"Done with {month}-{year}")

        # set field names for CSV file
        field_names = ['transaction_date','trade_date', 'ticker', 'company_name', 'owner_name', 'Title' ,'transaction_type', 'last_price', 'Qty', 'shares_held', 'Owned', 'Value']

        # Open a CSV file for writing
        with open('output_all_dates_monthly.csv', 'w', newline='') as f:
            print("writing")
            writer = csv.writer(f)

            # Write the column names in the first line of the CSV file
            writer.writerow(field_names)

            # Write the values of each transaction to the CSV file
            for transaction in all_data:
                writer.writerow(transaction)
                
# execute the function
get_openinsider_data()
print("Completed Process.")

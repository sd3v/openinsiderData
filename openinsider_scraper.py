import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor
import logging
import os
from datetime import datetime, timedelta

logger = logging.getLogger("my_logger")
logger.setLevel(logging.WARNING)
logger.addHandler(logging.FileHandler("logs.txt"))

OUTPUT_DIR = os.environ.get('OUTPUT_DIR', 'data')

def get_data_for_month(year, month):
    start_date = datetime(year, month, 1).strftime('%m/%d/%Y')
    end_date = (datetime(year, month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    end_date = end_date.strftime('%m/%d/%Y')
    print(f"processing month: {month}-{year}")
    data = set()
    url = f'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=-1&fdr={start_date}+-+{end_date}&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=5000&page=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        rows = soup.find('table', {'class': 'tinytable'}).find('tbody').findAll('tr')
    except:
        print("Error! Skipping")
        logger.error(f"This URL was not successful: {url}")
        return

    for row in rows:
        cols = row.findAll('td')
        if not cols:
            continue
        insider_data = {key: cols[index].find('a').text.strip() if cols[index].find('a') else cols[index].text.strip() 
                        for index, key in enumerate(['transaction_date', 'trade_date', 'ticker', 'company_name', 
                                                     'owner_name', 'Title', 'transaction_type', 'last_price', 'Qty', 
                                                     'shares_held', 'Owned', 'Value'])}
        data.add(tuple(insider_data.values()))
    return data

def get_openinsider_data():
    with ThreadPoolExecutor(max_workers=10) as executor:
        all_data = []
        current_year = datetime.now().year
        current_month = datetime.now().month
        for year in range(2013, current_year + 1):
            start_month = 1 if year != 2013 else 3
            end_month = current_month if year == current_year else 12
            for month in range(start_month, end_month + 1):
                futures = [executor.submit(get_data_for_month, year, month)]
                for future in futures:
                    all_data.extend(future.result())
                print(f"Done with {month}-{year}")

        field_names = ['transaction_date','trade_date', 'ticker', 'company_name', 'owner_name', 'Title' ,'transaction_type', 'last_price', 'Qty', 'shares_held', 'Owned', 'Value']

        # join filename with output directory
        output_file = os.path.join(OUTPUT_DIR, 'output_all_dates_monthly.csv')

        with open(output_file, 'w', newline='') as f:
            print("writing")
            csv.writer(f).writerow(field_names)
            for transaction in all_data:
                csv.writer(f).writerow(transaction)

# Execute the function
get_openinsider_data()
print("Completed Process.")

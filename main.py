import requests
from bs4 import BeautifulSoup
import json

def get_openinsider_data():
    # URL needs to be updated, just a test URL for now
    url = 'http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=&sich=&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find('table', {'class': 'tinytable'}).find('tbody').findAll('tr')

    data = []
    for row in rows:
        # skip rows without data
        if not row.findAll('td'):
            continue
        insider_data = {}
        insider_data['transaction_date'] = row.findAll('td')[1].find('a').text.strip()
        insider_data['ticker'] = row.findAll('td')[3].find('a').text.strip()
        insider_data['company_name'] = row.findAll('td')[4].find('a').text.strip()
        insider_data['owner_name'] = row.findAll('td')[5].find('a').text.strip()
        insider_data['transaction_type'] = row.findAll('td')[7].text.strip()
        insider_data['shares_traded'] = row.findAll('td')[8].text.strip()
        insider_data['last_price'] = row.findAll('td')[9].text.strip()
        insider_data['shares_held'] = row.findAll('td')[10].text.strip()

        data.append(insider_data)
    with open('output.json','w+') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

data = get_openinsider_data()

# OpenInsider Scraper

This Python script scrapes insider transaction data from openinsider.com and saves it to a CSV file named `output_all_dates_monthly.csv`. The script collects data for every month from January 2013 to the current month, using a multi-threaded approach to improve performance.

## Requirements

The script requires the following libraries to be installed:
- requests
- beautifulsoup4
- pandas
- concurrent.futures
- logging
- datetime

You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 pandas concurrent.futures logging datetime
```

## Usage
1. Clone the repository to your local machine.
2. Open the terminal and navigate to the directory where the repository is located.
3. Run the openinsider_scraper.py script:
```python
python openinsider_scraper.py
```
4. Wait for the script to finish. The data will be saved in a file named `output_all_dates_monthly.csv`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

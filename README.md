# OpenInsider Scraper

This Python script scrapes insider transaction data from openinsider.com and saves it to a CSV file named `output_all_dates_monthly.csv`. The script collects data for every month from January 2013 to the current month, using a multi-threaded approach to improve performance.

## Requirements

The script requires the following libraries to be installed:
- requests
- beautifulsoup4
- concurrent.futures
- logging
- datetime

You can install these libraries using pip:
```bash
pip install requests BeautifulSoup4 concurrent.futures logging datetime
```

## Usage
1. Clone the repository to your local machine.
2. Open the terminal and navigate to the directory where the repository is located.
3. Run the openinsider_scraper.py script:
```python
python openinsider_scraper.py
```
4. Wait for the script to finish. The data will be saved in a file named `output_all_dates_monthly.csv`.


### Detailed Description of the functionality
The `get_openinsider_data()` function is the main function that orchestrates the entire process of fetching and processing data for all months and years, and saving the output to a CSV file. Here's a breakdown of the steps:
- A `ThreadPoolExecutor` is created with a maximum of 10 workers. This will allow multiple requests to be sent at the same time, improving the overall speed of the program.
- An empty list called `all_data` is created to store all the data retrieved for all months and years.
- The current year and month are retrieved using the `datetime` module.
- The function iterates through all years and months from 2013 to the current year and month.
- For the first year (2013), the iteration starts from March, since the data before that is not available.
- For the current year, the iteration stops at the current month.
- For each year and month, a `get_data_for_month()` function is called with the year and month as arguments. The `ThreadPoolExecutor` ensures that multiple requests can be sent at the same time.
- The results of the `get_data_for_month()` function are added to the all_data list using the `extend()` method.
- After all months and years have been processed, the all_data list is written to a CSV file called `output_all_dates_monthly.csv`
- The column names for the CSV file are defined in the `field_names` variable.
- A CSV writer object is created using the `csv.writer()` method, and the column names are written to the first line of the CSV file using the `writerow()` method.
- The values of each transaction are written to the CSV file using the `writerow()` method.
- The `get_openinsider_data()` function is called, which starts the entire process.
- A message is printed to the console when the process is complete.




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License

[MIT](https://choosealicense.com/licenses/mit/)

# OpenInsider Data Scraper

A robust Python scraper for collecting insider trading data from openinsider.com.

## Features

- Multi-threaded data collection for high performance
- Intelligent caching system to minimize server load
- Configurable filters for transaction types and values
- Flexible data export in CSV and Parquet formats
- Comprehensive logging and error handling
- Automatic retry mechanism for failed requests
- Progress tracking with progress bar
- Docker support for easy deployment

## Installation

1. Clone the repository:
```bash
git clone git@github.com:sd3v/openinsiderData.git
cd openinsiderData
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

All settings are managed through `config.yaml`:

### Output Settings
```yaml
output:
  directory: data       # Output directory for scraped data
  filename: insider     # Base filename for output files
  format: csv          # Output format (csv or parquet)
```

### Scraping Settings
```yaml
scraping:
  start_year: 2024           # Start year
  start_month: 3             # Start month
  max_workers: 10            # Number of parallel downloads
  retry_attempts: 3          # Number of retry attempts
  timeout: 30               # Request timeout in seconds
```

### Filter Settings
```yaml
filters:
  min_transaction_value: 50000  # Minimum transaction value in USD
  transaction_types:            # Transaction types to include
    - P - Purchase
    - S - Sale
    - F - Tax
  exclude_companies: []         # Companies to exclude (by ticker)
  min_shares_traded: 100        # Minimum number of shares
```

### Logging Settings
```yaml
logging:
  level: INFO          # Logging level (DEBUG, INFO, WARNING, ERROR)
  file: scraper.log    # Log file name
  rotate_logs: true    # Enable log rotation
  max_log_size: 10     # Max log size in MB
```

### Cache Settings
```yaml
cache:
  enabled: true        # Enable caching
  directory: .cache    # Cache directory
  max_age: 24         # Cache max age in hours
```

## Usage

Run the scraper:
```bash
python openinsider_scraper.py
```

## Docker Support

Build the container:
```bash
docker build -t openinsider-scraper .
```

Run the container:
```bash
docker run -v $(pwd)/data:/app/data openinsider-scraper
```

## Transaction Types

Available transaction types:
- P - Purchase
- S - Sale
- F - Tax
- D - Disposition
- G - Gift
- X - Exercise
- M - Options Exercise
- C - Conversion
- W - Will/Inheritance
- H - Holdings
- O - Other

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting

- If you encounter rate limiting, adjust the `max_workers` setting
- For memory issues, try using Parquet format for large datasets
- Check the log file for detailed error messages

## Disclaimer

This tool is for educational purposes only. Ensure you comply with the website's terms of service and local regulations when scraping data.

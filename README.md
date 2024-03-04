# OpenInsider Scraper

If you've always wanted to dive into the riveting world of insider trading data, but were too lazy to manually sift through thousands of pages, then buckle up because you're in for a treat. This is your magic carpet to travel through time, from 2013 to the present, and gather juicy tidbits of insider trading data from the future, well not really, only up to the current month (if it could gather data from the future, I'd probably be on my yacht in the Caribbean by now). 

## What does this badboy do?

The code in this repository makes use of the requests and BeautifulSoup libraries in Python to scrape data from openinsider. The results are neatly tucked away in a CSV file. I also added threading so it's as fast as a leopard.

The script also comes with a built-in logger that logs events into a file because why not.

## How to Run

### Docker

Simply build the image and run:

```bash
docker buildx build -t openinsider ./
```

```bash
mkdir date
docker run -e OUTPUT_DIR="data" -v "${PWD}/data":data -it openinsider
```

You can also build the daily image and tell it when to start scraping:
```bash
docker buildx build -t openinsider-daily -f Dockerfile.daily
```

```bash
mkdir data
docker run -e OUTPUT_DIR="data" -e START_DATE="2024-03-01" -it openinsider-daily
```

### Bare python

Running the script is as easy as a walk in the park... on a sunny day... with your favorite ice cream in your hand. Clone the repository, make sure you have the required libraries installed:
```bash
pip install --upgrade pip
pip install requests BeautifulSoup4 logging datetime
```
and then just run the python script. Grab a cup of coffee, and watch it do the work. 

## Disclaimer

While this tool is quite powerful, it comes with no guarantee of making you rich. It will just make you *data* rich, which isn't necessarily the same thing. Also, this tool does not promote insider trading. It's called *insider trading data* scraper, not insider trading-data scraper.

## Last words

Enjoy the script and may the odds be ever in your favor!

FROM python:3-alpine 

# Install required packages
RUN apk add --update --no-cache \
    bash \
    python3 \
    && ln -sf python3 /usr/bin/python

RUN pip3 install --upgrade --no-cache \
    pip \
    BeautifulSoup4 \
    requests \
    datetime

COPY openinsider_scraper.py /openinsider_scraper.py

# expose volume /data
VOLUME /data

# Run the script as the entrypoint
CMD ["python3", "/openinsider_scraper.py"]


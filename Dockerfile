# FROM ubuntu:17.04
# FROM selenium/standalone-chrome
FROM python:3.9

WORKDIR /code

# requirements.txt has selenium and webdriver-manager packages. 
# they were added to the venv folder as : $python3 -m venv venv -> $. venv/bin/activate  -> $pip install webdriver-manager and all the other packages 
# $pip freeze > requirements.txt
# this creates a requirements.txt file 

COPY ./requirements.txt  /code/requirements.txt

RUN apt-get update && apt-get install unzip

# install Chrome
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#     && apt-get install ./google-chrome-stable_current_amd64.deb -y
    
# RUN apt-get install -y chromium-driver


# Update the package list and install chrome
RUN apt-get install -y wget
RUN apt --fix-broken install
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb

RUN pip install --no-cache-dir -r /code/requirements.txt
RUN pip install --no-cache-dir pandas selenium bs4 webdriver-manager


COPY ./src /code/src
COPY ./src/assets/chromedriver /code/src/assets/chromedriver

RUN chmod +x ./src/assets/chromedriver

CMD ["python", "src/main.py", "--host", "0.0.0.0", "--port", "11"]


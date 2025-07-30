# FROM nikolaik/python-nodejs:python3.10-nodejs19  <- This is based on old Debian Buster

# Use a newer image based on Debian Bullseye instead
FROM nikolaik/python-nodejs:python3.11-nodejs20-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ... rest of your Dockerfile

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start

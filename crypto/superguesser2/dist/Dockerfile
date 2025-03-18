FROM python:3.12-slim

RUN apt-get update \
    && apt-get install --no-install-recommends -y socat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pycryptodome

WORKDIR /app
COPY ./flag.txt /app/flag.txt
COPY ./chal.py /app/chal.py

USER nobody
CMD ["socat", "-T60", "TCP-LISTEN:1234,reuseaddr,fork", "EXEC:python3 chal.py,stderr"]

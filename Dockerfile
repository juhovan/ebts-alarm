FROM python:3.10.2-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD [ "python", "./main.py" ]

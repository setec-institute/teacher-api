FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

FROM python:3.8.10

WORKDIR /usr/src/app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install tensorflow

RUN pip install grpcio-tools

COPY . .

CMD [ "python", "./colors_server.py" ]
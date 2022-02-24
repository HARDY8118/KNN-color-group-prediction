# FROM python:3.8.10
# FROM tensorflow/tensorflow:latest-gpu
FROM tensorflow/tensorflow

WORKDIR /usr/src/app

# RUN pip install virtualenv

# ENV VENV=/usr/src/app/venv

# RUN python -m venv --system-site-packages $VENV

# RUN echo $PATH

# ENV PATH="$VENV/bin:$PATH"

# RUN echo $PATH

RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip
# RUN pip install tensorflow
RUN pip install grpcio
RUN pip install grpcio-tools

COPY . .

EXPOSE 50051

CMD [ "python", "colors_server.py" ]

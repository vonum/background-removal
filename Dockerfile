FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY tools ./tools
COPY libs ./libs
COPY setup.sh ./setup.sh
RUN ./setup.sh

COPY . ./
RUN mkdir images

CMD uvicorn --host 0.0.0.0 server:app
# CMD gunicorn -w 4 server:app

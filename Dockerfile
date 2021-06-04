FROM python:3.9.1
ADD src/ /src
WORKDIR /src
RUN pip install -r requirements.txt
FROM python:3.10.5
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 -m pip install -r requirements.txt
CMD ["python3","web.py"]
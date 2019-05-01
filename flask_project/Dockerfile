FROM python:3.7

RUN pip install --upgrade pip

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

RUN rm -r /root/.cache

WORKDIR /project/

CMD ["uwsgi", "--ini", "/project/uwsgi.ini"]

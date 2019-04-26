FROM python:3.7

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip install --upgrade pip


COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt


RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache
COPY nginx.conf /etc/nginx/
COPY mark-demo-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/


WORKDIR /project/


CMD ["/usr/bin/supervisord"]

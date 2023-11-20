FROM python:3.7-stretch

COPY ./ /opt/visapi


WORKDIR /opt/visapi

COPY sources.list /etc/apt/sources.list

RUN apt update && apt-get install -y vim libgfortran3

EXPOSE 8000

RUN pip install -r requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple


# Use https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
# hello world demo
FROM python:3.6
#代码添加到code文件夹
ADD . /code
# 设置code文件夹是工作目录
WORKDIR /code
# 安装支持

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN wget https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-x64.tar.xz
RUN xz -d node-v10.15.3-linux-x64.tar.xz
RUN tar -xvf node-v10.15.3-linux-x64.tar
RUN ln -s /node-v10.15.3-linux-x64/bin/node /usr/local/bin/node
RUN ln -s /node-v10.15.3-linux-x64/bin/npm /usr/local/bin/npm

COPY ./app /app
CMD ["python", "/app/main.py"]
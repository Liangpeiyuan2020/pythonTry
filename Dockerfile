# Use https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
# hello world demo
FROM python:3.8
#代码添加到code文件夹
ADD . /code
# 设置code文件夹是工作目录
WORKDIR /code
# 安装支持
COPY ./app /app

RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]
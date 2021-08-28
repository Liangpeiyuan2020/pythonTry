FROM python:3.6
#代码添加到code文件夹
ADD . /code
# 设置code文件夹是工作目录
WORKDIR /code

COPY requirements.txt requirements.txt
#按照requirements.txt文件安装依赖
RUN pip install -r requirements.txt
#从web获取node-v10.15.3-linux-x64.tar.xz
RUN wget https://npm.taobao.org/mirrors/node/v16.8.0/node-v16.8.0-linux-x64.tar.xz
#解压安装
RUN xz -d node-v16.8.0-linux-x64.tar.xz
RUN tar -xvf node-v16.8.0-linux-x64.tar.xz
#重命名
RUN mv node-v16.8.0-linux-x64 nodejs
#软连接
RUN ln -s /nodejs/bin/node /usr/local/bin/node
RUN ln -s /nodejs/bin/npm /usr/local/bin/npm
#复制项目到镜像
COPY ./app /app
#镜像执行入口
CMD ["python", "/app/main.py"]
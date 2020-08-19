FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

WORKDIR /usr/src/app
COPY . .

CMD [ "python3", "spider.py" ]
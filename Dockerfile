FROM python:3.6
WORKDIR /code
ENV FLASK_APP index.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY . .
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    apt-get update && \
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["flask", "run"]
# For more information, please refer to https://aka.ms/vscode-docker-python
# Dockerfile
FROM python:3.8

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

CMD ["python", "app.py"]

FROM python:3.6.1-alpine
RUN pip install requests
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]
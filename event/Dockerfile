FROM python:2

RUN pip install flask Flask-SQLAlchemy  SQLAlchemy-migrate  pymysql flask-restplus flask-restless

#RUN apt-get update && apt-get install -y sqlite
WORKDIR /root/UserApp/
ENV FLASK_APP app.py

COPY app /root/UserApp

CMD python app.py

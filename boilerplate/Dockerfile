FROM python:2

RUN pip install flask Flask-SQLAlchemy  SQLAlchemy-migrate  pymysql flask-restplus

RUN apt-get update && apt-get install -y sqlite
WORKDIR /root/UserApp/
ENV FLASK_APP app.py

#COPY UserApp /root/UserApp

CMD flask run --host=0.0.0.0

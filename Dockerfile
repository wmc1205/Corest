FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/wmc1205/Corest.git

RUN echo "testing1234"
WORKDIR /home/~/PycharmProjects/corest/

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
RUN echo "SECRET_KEY=django-insecure-hf*1^7d&_q6nr-cfc=l5$bhg!mu)^qx*k4neqq+&eh7ns)4ejf" > .env
RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
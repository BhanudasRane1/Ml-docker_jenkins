FROM centos:latest

FROM centos:latest

RUN yum install python3 -y

RUN pip3 install django

RUN pip3 install pillow

RUN pip3 install numpy

RUN pip3 install keras

RUN pip3 install tensorflow

RUN pip3 install requests

RUN pip3 install opencv-python



WORKDIR /app

COPY . /app


EXPOSE 8000

CMD python3 manage.py runserver



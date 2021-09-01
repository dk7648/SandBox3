FROM python:3.9.0

WORKDIR /home/

Run echo "eho"

RUN git clone https://github.com/dk7648/SandBox2.git

WORKDIR /home/SandBox2/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-)xi@a5e!2_u$+tcl@2o1#^+hsfrxh43&-_qm-z1p8hem1p^zf@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]


# FROM python:3.9.0
#
# WORKDIR /home/
#
# RUN echo "test ku sandbox!!"
#
# RUN git clone https://github.com/matt700395/kusandbox.git
#
# WORKDIR /home/kusandbox/
#
# RUN python -m pip install --upgrade pip
#
# RUN pip install -r requirements.txt
#
# RUN pip install gunicorn
#
# RUN pip install mysqlclient
#
# EXPOSE 8000
# python manage.py createsuperuser --settings=myproject.settings.deploy
#
# CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=web.settings.deploy && python manage.py migrate --settings=web.settings.deploy && gunicorn web.wsgi --env DJANGO_SETTINGS_MODULE=web.settings.deploy --bind 0.0.0.0:8000"]

FROM python:3.9.0

WORKDIR /home/

RUN echo "start1"

RUN git clone https://github.com/dk7648/hackathon_2021.git

WORKDIR /home/hackathon_2021/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=hackathon_2021.settings.deploy && python manage.py migrate --settings=hackathon_2021.settings.deploy && gunicorn hackathon_2021.wsgi --env DJANGO_SETTINGS_MODULE=hackathon_2021.settings.deploy --bind 0.0.0.0:8000"]

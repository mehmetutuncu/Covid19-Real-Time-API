FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y vim
RUN mkdir /code
WORKDIR /code
COPY requirements.pip /code/
RUN pip install -r requirements.pip
COPY . /code/
EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["gunicorn", "--chdir", "real_time_covid19_api", "--bind", ":8000", "real_time_covid19_api.wsgi:application"]
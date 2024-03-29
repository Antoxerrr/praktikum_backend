FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV APP_HOME=/home/app
ENV APP_SOURCES=/home/app/praktikum
RUN mkdir $APP_HOME

# Создаем файл под django логи
RUN mkdir $APP_HOME/logs
RUN touch $APP_HOME/logs/app.log

RUN apt update -y

WORKDIR $APP_HOME

COPY . $APP_HOME
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

RUN pip install uvicorn

WORKDIR $APP_SOURCES

RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh
ENTRYPOINT ["/home/app/entrypoint.sh"]

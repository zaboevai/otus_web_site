# Документация

# Info
Учебный проект.

Создание сайта с учебными курсами.


>http://127.0.0.1:8000

# Install

RabbitMQ:
>sudo apt-get install rabbitmq-server

requirements.txt:
>pip install -r requriments.txt

# Before run

Change celery EMAIL settings [otus_web_site/settings.py]()

>EMAIL_HOST = 'smtp.yandex.ru'

>EMAIL_PORT = 465

>EMAIL_USE_SSL = True

>DEFAULT_FROM_EMAIL = 'email'

>EMAIL_HOST_USER = 'login'

>EMAIL_HOST_PASSWORD = 'password'


# Run
Celery
> run_celery.sh

Web server
> run_server.sh

# Rest api

>Добавление новых пользователей:  

URL: [http://127.0.0.1:8000/api/auth/]()

{
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": ""
}

>Авторизация пользователя:  

URL: [http://127.0.0.1:8000/api/login/]()

{
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": ""
}

>Список курсов:  

URL: [http://127.0.0.1:8000/api/courses/]()

>Список курсов:  

URL: [http://127.0.0.1:8000/api/courses/1/]()


> GraphQl:  

URL: [http://127.0.0.1:8000/graphql/]()

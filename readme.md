# Документация

# Install

RabbitMQ:
>sudo apt-get install rabbitmq-server

requirements.txt:
>pip install -r requriments.txt

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

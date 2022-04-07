#Проект API для социальной сети Yatube
Позволяет создавать сользователей и посты, просматривать список групп, постов и своих подписок.
## Его автор [Анна](https://github.com/Bakarasik)

____
###Данный проект реализован с помощью: 
* Python 3.8
* Django 2.2
* Django rest framework 3.12
* JWT + Joser
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке.

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Далее на [странице с документацией](http://127.0.0.1:8000/redoc/) можно ознакомиться с примерами запросов и ответов на них.
____

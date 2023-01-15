# API для Yatube - спринт №9
## Описание
API приложение для социальной сети Yatube в которой реализованы следующие возможности:
* Публиковать записи и редактировать их;
* Комментировать записи;
* Подписываться/отписываться на авторов.

Подключиться к API сможет только аутентифицированный пользователь. Аутентификация осуществляется по токену(JWT).

### Документация для API Yatube
http://127.0.0.1:8000/redoc/


## Технологии
* Python 3.8
* Django 3.2
* SQLite3
* Django REST Framework (DRF)
* Django ORM
* Djoser


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Alexey-Roman/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```
source env/bin/activate
```

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python yatube_api\manage.py migrate
```

Запустить проект:

```bash
python yatube_api\manage.py runserver
```

## Примеры запросов

### Получить список постов:
```
GET .../api/v1/posts/
```
#### Ответ:
```
[
    {
        "id": 1,
        "author": "admin",
        "text": "Пост про историю",
        "pub_date": "2023-01-15T11:52:17.027632Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "admin",
        "text": "Пост про Космос",
        "pub_date": "2023-01-15T11:57:20.248009Z",
        "image": null,
        "group": null
    }
]
```


### Создать новый постов:
```
POST .../api/v1/posts/

Body:
{
    "text": "Пост про Улитку"
}
```
#### Ответ:
```
{
    "id": 3,
    "author": "admin",
    "text": "Пост про Улитку",
    "pub_date": "2023-01-15T11:59:27.872781Z",
    "image": null,
    "group": null
}
```


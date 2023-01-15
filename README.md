# API для Yatube - спринт №9
## Описание


## Технологии
* Python 3.8
* Django 3.2
* SQLite3
* Django REST Framework (DRF)
* Django ORM


### Как запустить проект:

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

### Документация для API Yatube
http://127.0.0.1:8000/redoc/
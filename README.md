# REST API для проекта TravelTube

## Описание
Простой, надежный и понятный API для социальной сети TravelTube.

## Технологии
Python 3,
Django 2.2,
Django REST Framework,
Simple-JWT

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Wests007/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/scripts/activate
```
Обновить менеджер пакетов и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в папку с файлом manage.py и выполнить миграции:
```
cd api_yatube
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

### Примеры запросов к API:

- Получение публикаций
GET /api/v1/posts/
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {...}
    ]
}
```

- Создание публикации
POST /api/v1/posts/

```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```


### В разработке:
Документация (ReDoc) всех возможных запросов/ответов API.

## Автор
[Ромашков Александр](https://github.com/Wests007)

# Тестовое задание

### **Стек**
![python version](https://img.shields.io/badge/Python-3.10-green)
![django version](https://img.shields.io/badge/Django-4.2.6-green)
![django_rest_framework version](https://img.shields.io/badge/DjangoRestFramework-3.14-green)

# Установка
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/iNTENSY/django-news-test.git
```


Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

# Примеры запросов
### Получение списка публикаций
Для получения списка всех публикаций необходимо отправить 
Get-запрос на адрес `http://127.0.0.1:8000/api/v1/news/`.

Пример ответа:
```
{
    "count": 23,
    "next": "http://127.0.0.1:8000/api/v1/news/?page=2",
    "previous": null,
    "results": [
        {
            "tag": [
                "Тег1"
            ],
            "title": "Заголовок 27",
            "text": "Текст 27",
            "visit_count": 0,
            "pk": 24
        },
        {
            "tag": [],
            "title": "Заголовок 23",
            "text": "Текст 23",
            "visit_count": 0,
            "pk": 23
        },
        {
            "tag": [],
            "title": "Заголовок 21",
            "text": "Текст 21",
            "visit_count": 0,
            "pk": 21
        }
    ]
}
```

### Добавление публикации
Для добавления новой публикации необходимо отправить POST-запрос
на адрес `http://127.0.0.1:8000/api/v1/news/` в JSON формате:

```
{
    "text": "Ваш текст",
    "group": 1
} 
```

### Добавление публикации
Для добавления новой публикации необходимо отправить DELETE-запрос
на адрес `http://127.0.0.1:8000/api/v1/news/<int:pk>/`.
В ответ ничего не возвращается.

# Автор
- Даценко Дмитрий
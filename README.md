# API for Upload files
Задание: Реализовать REST API для загрузки файлов и извлечения из них информации.


## Окружение проекта:
  * python 3.8
  * Django 4.0.3
  * djangorestframework

Склонируйте репозиторий с помощью git

    https://github.com/gogoshew/upload_api.git
Перейти в папку:
```bash
cd UploadFilesAPI
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


### Ссылка для загрузки файла client_org.xlsx:
http://127.0.0.1:8000/upload/clients/

### Ссылка для загрузки файла bills.xlsx:
http://127.0.0.1:8000/upload/bills/

### Ссылка для просмотра содержания файлов:
http://127.0.0.1:8000/api/clientlist/

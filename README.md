# FlSites
DRF приложение для для учета пользователей и организаций, в которых они состоят

Установка и запуск приложения

1. Создать папку приложения, установить в ней виртуальное окружение
python -m venv env
env\scripts\activate

2. Клонировать репозиторий
git clone https://github.com/AndrewFekl/FlSites.git .

3. Установить зависимости
pip install -r requirements.txt

4. Запустить приложение
python manage.py runserver

5. По адресу http://127.0.01:8000/docs/ изучит документацию по API

@echo off
cd /d "C:\Users\zhaka\PycharmProjects\Django-homework\"
call .venv\Scripts\activate.bat
python Task_4\manage.py runserver 192.168.0.14:8000
pause
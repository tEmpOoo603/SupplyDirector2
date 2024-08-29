- Склонируйте репозиторий и установите зависимости "pip install -r requirements.txt"-
- Создайте в postgresql пользователя с именем "root" и паролем "root", а также выдайте все разрешение
- Создайте базу данных postgresql с именем "file_system" и владельцем - root
- По умолчанию сервер postgresql запускается на локалхосте на порте 5432
- Примените все миграции "python manage.py migrate"
- Создайте суперпользователя для доступа к админке python manage.py createsuperuser
- запустить сервер "python manage.py runserver"
- В админке можно так же работать со всеми Ивентами и Изменениями ивентов 127.0.0.1:8000/admin/

# API реализован с префиксом /api/

- GET/POST/DELETE - folder/<folder_name>/ - посмотреть, создать или удалить папку
- POST - folder/<parent_folder_name>/<folder_name>/ - создать в папке parent_folder_name подпапку folder_name
- GET/POST/DELETE - file/<file_name>/ - посмотреть, создать или удалить файл
- POST - folder/<folder_name>/create-file/<file_name>/ - создать файл в указанной папке

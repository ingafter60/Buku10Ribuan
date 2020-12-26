# Buku10Ribuan
Membuat Ecommerce Flatform untuk Menjual Buku dengan Menggunakan Django
https://github.com/ingafter60/Buku10Ribuan

## CHAPTER 1 Introduction to Django

### Ch01 - 1. Initial setup - Create github repository

        modified:   README.md

### Ch01 - 2. Creating django project 'Buku10Ribuan' 

        >> Create root folder 'Buku10Ribuan'
        >> cd Buku10Ribuan
        >> pipenv --three install Django
        >> pipenv shell 
        >> django-admin startproject core .
        > Starting the Development Server
        >> python manage.py runserver
        new file:   Pipfile
        new file:   Pipfile.lock
        modified:   README.md
        new file:   core/__init__.py
        new file:   core/asgi.py
        new file:   core/settings.py
        new file:   core/urls.py
        new file:   core/wsgi.py
        new file:   manage.py

### Ch01 - 3. Create django app 'appmain' 

        > Create django app 'appmain'
        >> python manage.py startapp appmain
        > Registering appmain to settings
        modified:   README.md
        new file:   appmain/__init__.py
        new file:   appmain/admin.py
        new file:   appmain/apps.py
        new file:   appmain/migrations/__init__.py
        new file:   appmain/models.py
        new file:   appmain/tests.py
        new file:   appmain/views.py
        modified:   core/settings.py

































































































































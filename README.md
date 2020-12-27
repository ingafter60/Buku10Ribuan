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


### Ch01 - 4. Settings 

        > Install postgres driver
        >>  pipenv install psycopg2
        > Import os in settings 
        modified:   Pipfile
        modified:   Pipfile.lock
        modified:   README.md
        modified:   core/settings.py

## CHAPTER 2 Getting Started with a Simple Company Site

### Ch02 - 1. Starting with the Homepage

        modified:   README.md
        new file:   appmain/static/css/bootstrap.min.css
        new file:   appmain/static/js/bootstrap.min.js
        new file:   appmain/static/js/jquery.min.js
        new file:   appmain/static/js/popper.min.js
        new file:   appmain/templates/home.html
        modified:   core/urls.py


### Ch02 - 2. Adding an About Us Page, navigation and links

        modified:   .gitignore
        modified:   README.md
        new file:   appmain/templates/about_us.html
        new file:   appmain/templates/base.html
        modified:   appmain/templates/home.html
        new file:   appmain/urls.py
        modified:   core/urls.py

### Ch02 - 3. Creating a Contact Us Form

        modified:   README.md
        new file:   appmain/forms.py


### Ch02 - 4. Sending E-mails

        modified:   README.md
        modified:   core/settings.py


### Ch02 - 5. Adding the Form to the Contact Us Page

        modified:   README.md
        modified:   appmain/forms.py
        modified:   appmain/templates/base.html
        new file:   appmain/templates/contact_form.html
        modified:   appmain/urls.py
        modified:   appmain/views.py


### Ch02 - 6. Form Rendering

        modified:   README.md
        modified:   appmain/templates/contact_form.html




































































































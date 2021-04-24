# Student register app

## Requirement

In order to run this app, please install following packages / frameworks:

- django
- django-crispy-forms

```
python -m pip install Django
pip install django-crispy-forms
```

## How to run

Simply run following command:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then, access to `http://127.0.0.1:8000/student/list/` to list all students stored in the SQlite DB. All students are displayed in a table. You can also add new student or update / delete an existing student by clicking on `Add New` button or `Edit` icon or `Delete` icon respectively (on the last right column of the table).

## Remarks

- Date of birth must be in the format of `YYYY-MM-DD`. For example: `1986-06-21`.
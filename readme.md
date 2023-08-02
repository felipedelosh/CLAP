FelipedelosH
# Windows 10
Example Django

How to run:

Activate virtual ENV

0 -> GO cmd :HospitalAFH\env\Scripts> AND RUN: activate 

1 -> GO HospitalAFH PATH AND RUN: Python manage.py runserver

2 -> GO URL:
http://localhost:8000/clap/create/ 






Documentation
______
## 0 -> In terminal: 
Python -m vitualenv env
Enter in folder:
\env\Scripts 
And type inside folder:
activate

cd ..  cd ..

>Python3 -m pip  install --upgrade pip ?
pip install --upgrade pip ? 
pip install -r requirements.txt

## 1 -> RUN in CMD: Python -m pip install -r requirements.txt

## 2 -> Create a project:

django-admin startproject loQueSeaMierda .

# if you need run:

1 -> Activate a virtual env
\env\Scripts>activate

2 -> cd .. cd.. and run
Python manage.py runserver

3 -> enter the url:port


# If you need update database
Python manage.py makeMigration NewAPPName ?
Python manage.py migrate

# If you need create administrator user

Python manage.py createsuperuser

# if You need create a new app

Python manage.py startapp NewAPPName

and then install in: loQueSeaMierda\settings.py
INSTALLED_APPS.append(NewAPPName)
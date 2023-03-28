## Parts Arrival System

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)

Parts Arrival is an application built to accomodate the task and problems occur in parts distribution department or other company receiving area where there always an schedule and receiving problem in the end of the warehouse. Its a web based project where you can update and create arrival or monitor the arrival of certain parts and view the schedule and ETA (Estimated Time Arrive) of parts from the manufacturing.

It has built-in queing time in order to track upcoming parts from manufacturing that need to receive in the main warehouse in order to check its quality and can directly be tag to the warehouse.

## **Technology Used**

# Backend
 - PostgreSQL
 - Django 4.1
 - Gunicorn
 - Pipenv
 - Django Rest Framework (DRF)
# Frontend
 - Bootstrap4
 - FontAwesome (Icons and Fonts)

## **Installations**
```
 $ pip install pipenv
 $ pipenv shell
 $ pipenv install --all
 $ python manage.py migrate
 $ python manage.py runserver
```

```https://localhost:8000/```
## **Architecture**
Its an client to server architecture where you can migrate this in cloud based environment which compose of AWS (Amazon Web Services) or MS Azure (Microsoft Azure) platform  or more on premises that can be setup as an stand-alone software to be used by your end-user.

## **Licensing**
Its based on MIT Licensing which you can be allowed to distribute or sell this program and use existing code for modifacations and other stuff to address your needs or your company requirements that fit and compatible for your desired results.



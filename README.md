## Parts Arrival System

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework) ![Bitbucket Pipelines](https://img.shields.io/bitbucket/pipelines/enadheljhum/parts-arrival/master)

Parts Arrival is an internal tooling built-in to accomodate the task and problems occur in parts department or other company receiving area where there always an schedule and receiving problem in the end of the receiver. Its a web based project where you can update and create arrival or monitor the arrival of parts and view the schedule and ETA (Estimated Time Arrive) of parts.
You can add scheduling que to address the day to day task of checking the parts need to order or parts need to receive.


## **Technology Used**
 - PostgreSQL
 - Django 2.2
 - Gunicorn
 - Pipenv
 - Django Rest Framework (DRF)
 - Bootstrap4
 - Font-Awesome

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

## **Contributions**
As you know this project is under beta and doesnt accept contributions as of now as the author of this project will post announcement when the time to accept community contributions but you can still issue pull request and discuss whats break the project or bugs you been discovered in this project.

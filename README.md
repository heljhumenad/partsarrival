## Parts Arrival System

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)

Parts Arrival is an application built to accomodate the task and problems occur in parts distribution department or other company receiving area where there always an schedule and receiving problem in the end of the warehouse. Its a web based project where you can update and create arrival or monitor the arrival of certain parts and view the schedule and ETA (Estimated Time Arrive) of parts from the manufacturing.

It has built-in queing time in order to track upcoming parts from manufacturing that need to receive in the main warehouse in order to check its quality and can directly be tag to the warehouse.

## **Installations**
```
 $ pip install poetry 
 $ poetry install 
 $ poetry shell 
 $ python manage.py migrate
 $ python manage.py runserver
```

```https://localhost:8000/```


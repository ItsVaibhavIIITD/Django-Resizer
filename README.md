# Resizer

A REST API to add records and resize them on the fly!

## How to setup?
* Install Python 3.8.9
* Run `pip install virtualenv`
* Create a virtual environment using the command `virtualenv environment`
* Activate the virtual environment using the command `environment\Scripts\activate`. This will only work for Windows.
* Install the dependencies using the commnad `pip install -r requirements.txt`

## How to run the project?
* First, create some database migrations using the command `python manage.py makemigrations core` and then migrate them using the command `python manage.py migrate`
* Create a superuser using the command `python manage.py createsuperuser` and fill the required details.
* Admin panel can be accessed at this URL - `http://127.0.0.1:8000/admin/`
* Run the server using the command `python manage.py runserver`

## How job scheduling is implemented?

* In order to add job scheduling, a Python package, `APScheduler` is used. 

* The`APScheduler` is a lightweight task schedular for Python. The application performs resizing of all the enqueued requests or pending requests every `5` minutes.

* This duration can be edited by changing the `RESIZE` key of the `SCHEDULING_DURATION` setting.

## End Points

| S. No | API End Point | Request Type | Description | Status Code |
|---|---|---|---|---|
| 1 | `/records/` | GET | List all the existing records | 200 |
| 2 | `/records/add/` | POST | Add a new record | 201 |
| 3 | `/records/resize/all/` | POST | Resize all the pending records possibly before the scheduler does | 200 |
| 4 | `/records/resize/<int:id>/` | POST | Resize any existing record | 200 |
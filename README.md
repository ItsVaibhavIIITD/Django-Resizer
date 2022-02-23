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

## How to run unit tests?
* To run unit tests, use the command `python manage.py test`
* Unit tests also check the end point for resizing. If you'll explore the `uploads/fishes` directory after executing the above command, you will find a fish image that is scaled down to `140 x 93`. These dimensions are with respect to the `default.jpg` image provided in the files.

## How job scheduling is implemented?
* In order to add job scheduling, a Python package, `APScheduler` is used. 
* The`APScheduler` is a lightweight task schedular for Python. The application performs resizing of all the enqueued requests or pending requests every `5` minutes.
* This duration can be edited by changing the `RESIZE` key of the `SCHEDULING_DURATION` setting.

## How resizing is done?
* When a new record is added, a background job for the same is created. When the time comes, the image is retrieved, and resized with the help of Pillow package.
* While resizing the image, the aspect ratio of the image is maintained.
* The image won't exceed the dimensions 140 x 140.

## End Points

| S. No | API End Point | Request Type | Description | Status Code |
|---|---|---|---|---|
| 1 | `/records/` | GET | List all the existing records | 200 |
| 2 | `/records/add/` | POST | Add a new record | 201 |
| 3 | `/records/resize/all/` | POST | Resize all the pending records possibly before the scheduler does | 200 |
| 4 | `/records/resize/<int:id>/` | POST | Resize any existing record | 200 |

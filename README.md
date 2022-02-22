# Resizer

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
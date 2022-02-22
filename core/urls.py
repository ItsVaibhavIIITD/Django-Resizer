from django.urls import path
from core.views import add_record, records

urlpatterns = [
    path("records/add/", add_record, name = "add_record"),
    path("records/", records, name = "records"),
]
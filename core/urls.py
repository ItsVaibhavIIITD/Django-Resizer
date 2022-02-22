from django.urls import path
from core.views import add_record, records, resize_records, resize_record

urlpatterns = [
    path("records/add/", add_record, name = "add_record"),
    path("records/", records, name = "records"),
    path("records/resize/all/", resize_records, name = "resize_records"),
    path("records/resize/<int:id>/", resize_record, name = "resize_record"),
]
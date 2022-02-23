import json
import random
from rest_framework import status
from core.models import Record, BackgroundJob
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

class RecordTestCase(APITestCase):
    def setUp(self):
        self.list_records_url = reverse("records")
        self.add_record_url = reverse("add_record")
        self.resize_all_url = reverse("resize_records")
        self.records_count = 0  
        self.path = str(settings.MEDIA_ROOT) + "\\" + "fishes\default.jpg"      
        self.data = {
            "name": f"name",
            "species": f"species",
            "weight": random.randint(10, 100),
            "length": random.randint(10, 100),
            "latitude": random.randint(-90, 90),
            "longitude": random.randint(-90, 90),
            "timestamp": timezone.now()
        }

        for i in range(random.randint(5, 10)):
            Record.objects.create(
                name = f"name-{i}",
                image = f"fishes/default.jpg",
                species = f"species-{i}",
                weight = random.randint(10, 100),
                length = random.randint(10, 100),
                latitude = random.randint(-90, 90),
                longitude = random.randint(-90, 90),
                timestamp = timezone.now()
            )
            self.records_count += 1

    def tearDown(self):
        pass
    
    def test_list_records(self):
        response = self.client.get(self.list_records_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.records_count)

    def test_add_record(self):
        with open(self.path, "rb") as image:
            self.data["image"] = image
            response = self.client.post(self.add_record_url, self.data)
            id = response.data["id"]
            self.data["image"] = None
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(BackgroundJob.objects.all().count(), 1)
            response = self.client.post(self.resize_all_url, {})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(BackgroundJob.objects.all().count(), 0)
            Record.objects.get(id = id).delete()
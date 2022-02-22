from rest_framework import serializers
from core.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["id", "name", "image", "species", "weight", "length", "latitude", "longitude", "timestamp"]

    def get_image_url(self, instance):
        request = self.context.get("request")
        return request.build_absolute_uri(instance.fingerprint.url)
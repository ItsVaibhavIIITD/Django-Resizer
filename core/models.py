from django.db import models
from secrets import token_hex
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.validators import MinValueValidator

def record_filename(instance, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (token_hex(32), extension)
    return f"fishes/{filename}"

class Record(models.Model):
    name = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = record_filename, null = False, blank = False)
    species = models.CharField(max_length = 100)
    weight = models.FloatField(default = 0.0, validators = [MinValueValidator(0.0)], verbose_name = "Weight (kg)")
    length = models.FloatField(default = 0.0, validators = [MinValueValidator(0.0)], verbose_name = "Length (cm)")
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    timestamp = models.DateTimeField()

@receiver(pre_delete, sender = Record)
def record_delete(sender, instance, *args, **kwargs):
    instance.image.delete(save = False)

class BackgroundJob(models.Model):
    record = models.OneToOneField(Record, on_delete = models.CASCADE, related_name = "job")
import os
from PIL import Image
from django.conf import settings
from core.models import BackgroundJob, Record

def resize(instance):
    if isinstance(instance, BackgroundJob):
        path = str(instance.record.image)
    elif isinstance(instance, Record):
        path = str(instance.image)

        try:
            instance.job.delete()
        except:
            pass

    path = path.replace("/", "\\")
    path = str(settings.MEDIA_ROOT) + "\\" + path
    image = Image.open(path)
    w = image.size[0]
    h = image.size[1]        

    if w >= h:
        ratio = w / h
        w = 140
        h = 140 / ratio
    else:
        ratio = h / w
        w = 140 / ratio
        h = 140
    
    image = image.resize((round(w), round(h)))
    image.save(path)

def resize_job():
    tasks = BackgroundJob.objects.all()
    records = []

    for t in tasks:
        resize(t)
        records.append(t.record.name)

    tasks.delete()
    return records
import os
from PIL import Image
from django.conf import settings
from core.models import BackgroundJob

def resize_job():
    tasks = BackgroundJob.objects.all()

    for t in tasks:
        path = str(t.record.image)
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

    tasks.delete()
from core.utils import resize_job
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

def start():
    scheduler = BackgroundScheduler(timezone = "Asia/Kolkata")
    scheduler.add_job(resize_job, trigger = "interval", minutes = settings.SCHEDULING_DURATION["RESIZE"], id = "image-resize-101", replace_existing = True)
    scheduler.start()
from core.utils import resize_job
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler(timezone = "Asia/Kolkata")
    scheduler.add_job(resize_job, trigger = "interval", minutes = 5, id = "image-resize-101", replace_existing = True)
    scheduler.start()
    scheduler.print_jobs()
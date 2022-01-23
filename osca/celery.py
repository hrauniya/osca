import os

from celery import Celery
import subprocess


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls quickstart every 100 seconds.
    sender.add_periodic_task(100.0, test.s('hello'), name='add every 10')
    #Refreshes database!

@shared_task
def updatesheet():
    subprocess.check_call(['python', 'quickstart.py'])
    return



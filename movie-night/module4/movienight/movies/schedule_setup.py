from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask

def schedule_setup():
    schedule, created =IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES,every=1)
    pt = PeriodicTask.objects.create(name="Minute",interval=schedule,task="movies.tasks.notify_of_starting_soon")
from django.db import models
from apps.utils.models import TimeStamps


class Lecture(TimeStamps):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecture_name = models.CharField(
        max_length=100,
        default='',
        blank=True,
        null=True)
    durations = models.IntegerField(
        help_text='Enter number of hours',)
    date = models.DateField()
    slides_urls = models.CharField(max_length=255)

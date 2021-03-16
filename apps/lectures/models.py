from django.db import models
from apps.utils.models import TimeStamps


class Lecture(TimeStamps):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    slides_urls = models.CharField(max_length=255)

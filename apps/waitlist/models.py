from django.db import models

# Create your models here.
from apps.utils.models import TimeStamps


class WaitlistEntry(TimeStamps):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'WaitlistEntries'

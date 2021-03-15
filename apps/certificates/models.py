from django.db import models
from apps.utils.models import TimeStamps

# Create your models here.
class Certificate(TimeStamps):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

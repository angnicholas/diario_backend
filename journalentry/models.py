from django.db import models
from authapi.models import User

# Create your models here.


class JournalEntry(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=20000)

    sentiment = models.JSONField(null=True, blank=True)
    # summary = models.CharField(max_length=10000, blank=True, null=True)
    # critical_alert = models.JSONField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

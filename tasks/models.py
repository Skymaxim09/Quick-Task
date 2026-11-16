from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
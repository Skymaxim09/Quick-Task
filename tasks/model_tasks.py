from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    user = models.ForeignKey(
        
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(default=True,max_length=200)
    description = models.CharField(null=True,blank=True,max_length=200)
    status = models.CharField(default="Pending",max_length=100)
    priority = models.CharField(default="Medium",max_length=100)
    due_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    

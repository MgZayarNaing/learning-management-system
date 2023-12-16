from email.policy import default
from django.db import models
from datetime import datetime
from my_app import enums
from django.utils import timezone
# Create your models here.

class FilesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    file = models.FileField(default=None)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
    
class RolesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
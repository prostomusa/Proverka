from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50, db_index=True, unique=True)
    password = models.CharField(max_length=50, db_index=True)

# Create your models here.

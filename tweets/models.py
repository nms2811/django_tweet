from django.db import models

# Create your models here.

class Tweet(models.Model):
    #Maps to SQL
    #id = models.AutoField(primary_key=True)
    content = models.TextField(blank = True, null = True)
    image = models.FileField(upload_to='images/', blank = True, null = True)

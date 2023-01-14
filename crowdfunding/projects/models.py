from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField() #checking whether the project is active or not
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=200)
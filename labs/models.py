from django.db import models

# Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    preview = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
from email.mime import image
from django.db import models
import django.utils.timezone
class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField(auto_now=False)
    
    
    def __str__(self):
        return self.title

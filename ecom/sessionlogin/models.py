from django.db import models

# Create your models here.
class Session(models.Model):
    username = models.CharField(max_length=29)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    

    def __str__(self):
        return self.username + ' ' + self.email
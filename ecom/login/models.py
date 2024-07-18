from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    file = models.FileField(max_length=230, upload_to='uploads/')

    def __str__(self):
        return self.name + '' + self.last_name

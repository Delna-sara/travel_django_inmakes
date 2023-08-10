from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class team_members(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField()
    profile_pic=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


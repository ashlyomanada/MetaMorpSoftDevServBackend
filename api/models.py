from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title

class WeDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title

class ChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title
from django.db import models
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=100)
    izoh=models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    izoh=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('detail',args=[str(self.pk)])
from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('news:mainPage',kwargs={'pk':self.pk})
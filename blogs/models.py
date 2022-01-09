from django.db import models
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=2000000000,  default="", blank=False)
    shortTitle = models.CharField(
        max_length=2000000000,  default="", blank=False)
    introPara = models.TextField(default="", blank=False)
    slug = models.CharField(max_length=2000000000,  default="", blank=False, primary_key = True)
    introimage = models.TextField(default="", blank=False)

    def __str__(self):
        return self.title + " : " + self.slug

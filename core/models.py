from django.db import models

# Create your models here.


class Agenda(models.Model):
    title = models.CharField(max_length=200, blank=True, primary_key = True)
    description = models.TextField(max_length=400, blank=True)
    year = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.year + ' : ' + self.title


class Member(models.Model):
    firstName = models.CharField(max_length=200, blank=True, primary_key = True)
    lastName = models.CharField(max_length=200, blank=True)
    stream = models.CharField(max_length=200, blank=True)
    course = models.CharField(max_length=200, blank=True)
    year = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=200, blank=True)
    deptName = models.CharField(max_length=200, blank=True)
    quote = models.TextField(max_length=400, blank=True)
    posnum = models.CharField(max_length=10, blank=True)
    linkedIn = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + f' ({self.deptName}) - ' + self.year

    def get_model_fields(self, model):
        return model._meta.fields

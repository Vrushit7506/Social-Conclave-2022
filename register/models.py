from django.db import models
from phone_field import PhoneField
from django.core import validators
from django.utils import timezone

# Create your models here.


class Delegate(models.Model):
    topic = (
        ('Affordable and Clean Energy', 'Affordable and Clean Energy'),
        ('Rural Healthcare', 'Rural Healthcare'),
        ('Sustainability of Consumer Goods', 'Sustainability of Consumer Goods'),
        ('Women`s Safety and Vigilance', 'Women`s Safety and Vigilance'),
    )
    genderChoices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non binary', 'Non binary'),
        ('Prefer not to Disclose', 'Prefer not to Disclose'),
    )

    teamyn = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    mumbai = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    counter = models.IntegerField(primary_key=True, default=None)
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(
        blank=False, choices=genderChoices, max_length=200, default=None)
    phoneNumber = models.CharField(max_length=10, blank=True)
    altphoneNumber = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=200,  blank=True)
    dob = models.CharField(max_length=10, blank=True)
    topicPref1 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    topicPref2 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    topicPref3 = models.CharField(
        max_length=2000, choices=topic,  blank=False, default=None)
    schoolName = models.CharField(max_length=1000, blank=True)
    pastexp = models.CharField(max_length=1000, blank=True)
    teamyn = models.CharField(
        max_length=2000, choices=teamyn,  blank=False, default=None)
    mumbai = models.CharField(
        max_length=2000, choices=mumbai,  blank=False, default=None)
    team = models.CharField(max_length=1000,blank=True)
    registeredBy = models.CharField(max_length=1000,blank=True)
    Paid = models.BooleanField(blank=False, default=False)
    TnC = models.BooleanField(blank=True, default=False)
    timeRegistered = models.DateTimeField(default=timezone.now,null=True)
    def __str__(self):
        return "SC" + "{:03d}".format(self.counter) + ' : ' + self.name
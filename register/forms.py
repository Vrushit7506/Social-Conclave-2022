from django import forms
from .models import *
from django.core import validators


class DelegateForm(forms.ModelForm):
    class Meta:
        model = Delegate
        fields = ['name', 'age', 'email', 'phoneNumber', 'address',
                  'gender', 'topicPref1', 'topicPref2', 'topicPref3', 'city', 'schoolName', 'courseName','yearGrad','team','registeredBy']
        labels = {
            "name": "",
            "age": "",
            'email': '',
            "phoneNumber": "",
            "address": "",
            'gender': 'Gender',
            "topicPref1": "Enter First Preference",
            "topicPref2": "Enter Second Preference",
            "topicPref3": "Enter Third Preference",
            "city": "",
            "schoolName": "",
            "courseName": "",
            "yearGrad": "",
            'team':'',
            'registeredBy':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'required': 'required'}),

            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Contact Number', 'required': 'required'}),

            'schoolName': forms.TextInput(attrs={'placeholder': 'College Name', 'required': 'required'}),

            'address': forms.Textarea(attrs={'placeholder': 'Address: (Please include nearest landmark and pincode)', 'required': 'required', 'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': 'required'}),

            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'required': 'required'}),

            'city': forms.TextInput(attrs={'placeholder': 'Country', 'required': 'required'}),

            'courseName': forms.TextInput(attrs={'placeholder': 'Course'}),

            'yearGrad': forms.NumberInput(attrs={'placeholder': 'Year Of Graduation', 'required': 'required'}),
            'registeredBy':forms.TextInput(attrs={'placeholder':'Registered By: '}),
            'gender': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'team': forms.TextInput(attrs={'placeholder': 'Team name: (If arriving with one)', 'required': 'required'}),
            'topicPref1': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref2': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref3': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
        }

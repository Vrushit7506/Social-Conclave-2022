from django import forms
from .models import *
from django.core import validators
from django.contrib.auth import get_user_model

Delegates = get_user_model()

class DelegateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DelegateForm, self).__init__(*args, **kwargs)
        self.fields['counter'].required = False
    class Meta:
        model = Delegate
        fields = ['counter', 'name', 'age', 'email', 'phoneNumber', 'address',
                  'gender', 'topicPref1', 'topicPref2', 'topicPref3', 'city', 'schoolName', 'courseName','yearGrad','team','registeredBy', 'TnC']
        labels = {
            "name": "",
            "age": "",
            'email': '',
            "phoneNumber": "",
            "address": "Enter Your Address",
            'gender': 'Gender',
            "topicPref1": "Enter First Topic Preference",
            "topicPref2": "Enter Second Topic Preference",
            "topicPref3": "Enter Third Topic Preference",
            "city": "",
            "schoolName": "",
            "courseName": "",
            "yearGrad": "",
            'team':'',
            'registeredBy':'',
            'TnC': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce semper laoreet placerat. Nullam semper auctor justo, rutrum posuere odio vulputate nec.',
        }
        widgets = {
            'counter': forms.HiddenInput(),

            'name': forms.TextInput(attrs={'placeholder': 'Name', 'required': 'required'}),

            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Contact Number', 'required': 'required'}),

            'schoolName': forms.TextInput(attrs={'placeholder': 'College Name', 'required': 'required'}),

            'address': forms.Textarea(attrs={'placeholder': 'Address: (Please include nearest landmark and pincode)', 'required': 'required', 'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': 'required'}),

            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'required': 'required'}),

            'city': forms.TextInput(attrs={'placeholder': 'City', 'required': 'required'}),

            'courseName': forms.TextInput(attrs={'placeholder': 'Course'}),

            'yearGrad': forms.NumberInput(attrs={'placeholder': 'Year Of Graduation', 'required': 'required'}),
            'registeredBy':forms.TextInput(attrs={'placeholder':'Registered By: '}),
            'gender': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'team': forms.TextInput(attrs={'placeholder': 'Team name: (If arriving with one)', 'required': 'required'}),
            'topicPref1': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref2': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref3': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'TnC': forms.CheckboxInput(attrs={'placeholder': '', 'required': 'required'})
        }
        

    def clean_email(self):
        email = self.cleaned_data["email"]
        user_count = Delegate.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("This Email Has Already Been Registered.")
        return email

    def clean_phoneNumber(self):
        phoneNumber = self.cleaned_data["phoneNumber"]
        print(len(phoneNumber))
        if len(phoneNumber) != 10:
            raise forms.ValidationError("Please Enter Your Phone Number Correctly.")
        user_count = Delegate.objects.filter(phoneNumber=phoneNumber).count()
        if user_count > 0:
            raise forms.ValidationError("This Phone Number Has Already Been Registered.")
        return phoneNumber

    def save(self, commit=True):
        # topicPref1 = self.cleaned_data["topicPref1"]
        # topicPref2 = self.cleaned_data["topicPref2"]
        # topicPref3 = self.cleaned_data["topicPref3"]
        # if topicPref1 == topicPref2 or topicPref1 == topicPref3:
        #     print("ERROR")
        #     raise forms.ValidationError("Your Topic Preferences Are Repeated.")

        i = Delegate.objects.all().order_by('-counter')[0]
        self.counter = i.counter+1
        self.counter = "{:03d}".format(self.counter)
        user = super(DelegateForm, self).save(commit=False)
        user.save()

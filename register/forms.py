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
        fields = ['counter', 'name', 'phoneNumber', 'altphoneNumber', 'email', 'dob', 'schoolName',
                  'gender', 'topicPref1', 'topicPref2', 'topicPref3', 'teamyn','team','mumbai','registeredBy', 'pastexp', 'TnC']
        labels = {
            "name": "",
            'phoneNumber': '',
            "altphoneNumber": "",
            "email": "",
            "dob": "",
            'gender': 'Gender',
            "schoolName": "",
            "topicPref1": "Enter First Topic Preference",
            "topicPref2": "Enter Second Topic Preference",
            "topicPref3": "Enter Third Topic Preference",
            "pastexp": "",
            "teamyn": "Team? ",
            "team": "",
            "mumbai": "Residing in Mumbai? ",
            'registeredBy':'',
            'TnC': 'The Email Address Provided Above Will Be Used For Further Communication And Steps.',
        }
        widgets = {
            'counter': forms.HiddenInput(),

            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': 'required'}),

            'phoneNumber': forms.NumberInput(attrs={'placeholder': 'Mobile Number', 'required': 'required'}),

            'altphoneNumber': forms.NumberInput(attrs={'placeholder': 'Alternate Mobile Number', 'required': 'required'}),

            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'required': 'required'}),

            'dob': forms.TextInput(attrs={'placeholder': 'Date of Birth (DD-MM-YYYY)', 'required': 'required'}),

            'gender': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),

            'schoolName': forms.TextInput(attrs={'placeholder': 'College Name / School Name / Company Name', 'required': 'required'}),

            # 'address': forms.Textarea(attrs={'placeholder': 'Address: (Please include nearest landmark and pincode)', 'required': 'required', 'class': 'form-control'}),

            'topicPref1': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref2': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),
            'topicPref3': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),

            'pastexp': forms.TextInput(attrs={'placeholder': 'Past Experience'}),

            'teamyn': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),

            'team': forms.TextInput(attrs={'placeholder': 'Team name: (If arriving with one, otherwise Enter "NA")'}),
            

            'mumbai': forms.RadioSelect(attrs={'placeholder': '', 'required': 'required'}),

            'registeredBy':forms.TextInput(attrs={'placeholder':'Registered by / How did you hear about us?'}),
            
            
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

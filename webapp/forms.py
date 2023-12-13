from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Add a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['Name', 'Email', 'Notes']


# Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['Name', 'Email', 'Notes']
""""
class DeleteRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['Submit','Cancel']
"""

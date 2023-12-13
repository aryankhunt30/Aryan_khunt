from django.db import models
from django import forms
from django.core import validators
from django.urls import reverse


class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    Name = models.CharField(max_length=100, unique=True)

    Email = models.EmailField(validators=[validators.EmailValidator(message="Invalid Email")], unique=True)

    Notes = models.CharField(max_length=500)


    def __str__(self):

        return self.Name 


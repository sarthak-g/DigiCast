from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField

# Create your models here.

class CredentialsModel(models.Model):
    credential = CredentialsField()
    title = models.CharField(max_length=30,default='')
    description = models.CharField(max_length=30,default='')

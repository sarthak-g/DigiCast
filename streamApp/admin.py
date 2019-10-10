from django.contrib import admin
from .models import CredentialsModel,BlockChainModel
# Register your models here.

admin.site.register([CredentialsModel, BlockChainModel])

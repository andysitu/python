from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Hours(models.Model):
    date = models.DateTimeField()

    hours = models.IntegerField(default=0)

    types = models.ManyToManyField(Type)

    def __str__(self):
        return str(self.date)
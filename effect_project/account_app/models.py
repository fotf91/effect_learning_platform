from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
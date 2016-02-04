from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager
class EmailBasedUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                date_of_birth=date_of_birth,)
        user.is_superuser = True # without this line the admin does not give any permission to edit
        user.is_admin = True
        user.save(using=self._db)
        return user


class EmailBasedUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = EmailBasedUserManager()

    def get_full_name(self):
    #     the user is identified by the email address
        return self.email

    def get_short_name(self):
    #     the user is identified by the email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, obj=None):
        "Does the user have a specific permission?"
        # todo: fix the following
        # simplest possible answer: yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # todo: fix the following
        # Simplest possible answer: All admins are staff
        return self.is_admin

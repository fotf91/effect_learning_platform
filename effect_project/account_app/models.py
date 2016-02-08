from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


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
    user_type = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(2), MinValueValidator(1)]
     )
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


class TypeGUser(models.Model):
    """
    TypeGUser represents the Graduate user
    """
    # one to one relationship to the EmailBasedUser
    user = models.OneToOneField(EmailBasedUser, null = True)
    # basic info
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True)
    passion = models.CharField(max_length=255, blank=True)
    alumn = models.BooleanField(default = False)
    # phone number regular expression and field
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=20) # validators should be a list
    # info about education
    education_val1 = models.CharField(max_length=255, blank=True)
    education_val2 = models.CharField(max_length=255, blank=True)
    education_val3 = models.CharField(max_length=255, blank=True)
    # info about experience
    experience_val1 = models.CharField(max_length=255, blank=True)
    experience_val2 = models.CharField(max_length=255, blank=True)
    experience_val3 = models.CharField(max_length=255, blank=True)
    # info about top skills
    skill_top_val1 = models.CharField(max_length=255, blank=True)
    skill_top_val2 = models.CharField(max_length=255, blank=True)
    skill_top_val3 = models.CharField(max_length=255, blank=True)
    # info about secondary skills
    skill_secondary_val1 = models.CharField(max_length=255, blank=True)
    skill_secondary_val2 = models.CharField(max_length=255, blank=True)
    skill_secondary_val3 = models.CharField(max_length=255, blank=True)
    # info about the expertise area
    expertise_area_val1 = models.CharField(max_length=255, blank=True)
    expertise_area_val2 = models.CharField(max_length=255, blank=True)
    expertise_area_val3 = models.CharField(max_length=255, blank=True)


class TypeCUser(models.Model):
    """
    TypeGUser represents the Company user
    """
    # one to one relationship to the EmailBasedUser
    user = models.OneToOneField(EmailBasedUser, null = True)
    # basic info
    official_name = models.CharField(max_length=255)
    # basic info of the person responsible
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # phone number regular expression and field
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=20) # validators should be a list
    # tagline-passion-philosophy of the company
    tagline = models.CharField(max_length=255, blank=True)
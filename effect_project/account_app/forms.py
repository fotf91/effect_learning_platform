from django import forms
from account_app.models import (EmailBasedUser, TypeGUser, TypeCUser)
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class GeneralUserCreationForm(forms.ModelForm):
    """
    Registration
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    CHOICES = (('1', '1',), ('2', '2',))
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)

    class Meta:
        model = EmailBasedUser
        fields = ('email', 'user_type')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(GeneralUserCreationForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class GeneralUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = EmailBasedUser
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AuthenticationForm(forms.Form):
    """
    Login form using the EmailBasedUser model
    """
    class Meta:
        fields=['email', 'password']


class EditTypeGUserForm(forms.ModelForm):
    class Meta:
        model = TypeGUser
        fields = ('first_name',
                  'last_name',
                  # 'date_of_birth',
                  'status',
                  'passion',
                  'location',
                  # 'phone_number',
                  'education_val1',
                  'education_val2',
                  'education_val3',
                  'skill_top_val1',
                  'skill_top_val2',
                  'skill_top_val3',
                  'skill_secondary_val1',
                  'skill_secondary_val2',
                  'skill_secondary_val3',
                  # 'expertise_area_val1',
                  # 'expertise_area_val2',
                  # 'expertise_area_val3',
                  # 'avatar',
                  )


class EditTypeCUserForm(forms.ModelForm):
    class Meta:
        model = TypeCUser
        fields = ('official_name',
                  'first_name',
                  'last_name',
                  'avatar',
                  'date_of_birth',
                  'tagline',
                  'phone_number',
                  'position',
                  )
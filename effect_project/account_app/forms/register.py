from django import forms
from account_app.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.widget.TextInput,
                             label='Email')
    password1 = forms.CharField(widget=forms.widget.PasswordInput,
                                label='Password')
    password2 = forms.CharField(widget=forms.widget.PasswordInput,
                                label='Password')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
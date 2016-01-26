from django import forms


class AuthenticationForm(forms.Form):
    """
    Login Form
    """
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']
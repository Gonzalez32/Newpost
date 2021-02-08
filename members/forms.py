from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    first_name = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'



class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    # date_joined= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_superuser', 'is_staff', 'is_active')

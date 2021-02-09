from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms 
from main_app.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'linkedin_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Bio...'}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'website_url': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Url...'}),
            'facebook_url': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Url...'}),
            'twitter_url': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Url...'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Url...'}),
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))

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


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

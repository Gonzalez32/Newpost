from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Title...'}),
            'author': forms.Select(attrs={'class': 'select is-warning'}),
            'body': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Post...'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Title...'}),
            # 'author': forms.Select(attrs={'class': 'select is-warning'}),
            'body': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Post...'}),
        }
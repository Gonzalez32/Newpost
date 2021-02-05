from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Title...'}),
            'author': forms.Select(attrs={'class': 'select is-warning'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'select is-warning'}),
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
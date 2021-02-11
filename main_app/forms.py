from django import forms
from .models import Post, Category, Comment


# choices = Category.objects.all().values_list('name', 'name')

# choices_list = []

# for item in choices:
#     choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Title...'}), 
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            # 'category': forms.SelectInput(choices=choices_list, attrs={'class': 'select is-warning'}),
            'category': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Category'}),
            'body': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Post...'}),
            'snippet': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Snippet...'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Title...'}),
            'body': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Post...'}),
            'snippet': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Post...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input is-warning', 'placeholder': 'Enter Name...'}),
            'body': forms.Textarea(attrs={'class': 'textarea is-warning', 'placeholder': 'Enter Comment...'}),
        }
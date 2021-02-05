from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
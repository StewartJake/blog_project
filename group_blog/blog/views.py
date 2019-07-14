from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                   DetailView, CreateView,
                                   UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post


    #like a sql query in py3
    #grab all objects in post model
    #filter based on conds
    def get_queryset(self):
        return (Post.objects.filter(published_date__lte=timezone.now)
                                    .order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    for_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return (Post.objects.filter(published_date__isnull=True)
                                    .order_by('created_date'))

"""group_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),
            name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    re_path('post/(?P<pk>\d+)$/edit/$', views.UpdatePostView.as_view(),
            name='post_edit'),
    re_path('post/(?P<pk>\d+)$/delete/$', views.DeletePostView.as_view(),
            name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]

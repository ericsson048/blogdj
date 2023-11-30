from django.contrib.auth.decorators import login_required
from django.urls import path
from posts.views import BlogPostHome, BlogPostCreate, BlogPostUpdate, BlogPostDetails, BlogPostDelete

app_name = "posts"

urlpatterns = [
    path('', BlogPostHome.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetails.as_view(), name='post'),
    path('edit/<str:slug>', login_required(BlogPostUpdate.as_view()), name='edit'),
    path('delete/<str:slug>',login_required(BlogPostDelete.as_view()), name='delete'),

]
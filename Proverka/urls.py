"""Proverka URL Configuration

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
from django.urls import path
from bank import views
from .views import redirect_blog
from bank.centerbank import *
from django.views.generic import TemplateView
euro1 = euro()
dollar1 = dollar()
urlpatterns = [
    path('', redirect_blog),
    path('rate/', TemplateView.as_view(template_name="bank/rate.html", extra_context={"dollar": dollar1, "euro": euro1}), name='rate'),
    path('admin/', admin.site.urls),
    path('blog/<str:slug>/update', views.PostUpdate.as_view(), name='post_update_url'),
    path('blog/<str:slug>/delete', views.PostDelete.as_view(), name='post_delete_url'),
    path('blog/create', views.PostCreate.as_view(), name='post_create_url'),
    path('blog', views.post_list, name='our_blog'),
    path('blog/<str:slug>', views.Postn.as_view(), name='post_detail'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/create', views.TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/update', views.TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete', views.TagDelete.as_view(), name='tag_delete_url'),
    path('tags/<str:slug>', views.Tagn.as_view(), name='tag_detail'),
]

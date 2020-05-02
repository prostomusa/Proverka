from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .utils import *
from django.views.generic import View
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):

    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = "?page={}".format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    #http://127.0.0.1:8000/blog/?page=
    return render(request, 'bank/reg.html', context=context)

class Postn(ObjectDetailMixin, View):
    model = Post
    template = 'bank/detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'bank/tags_list.html', context={'tags': tags})

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'bank/post_create.html'
    raise_exception = True

class Tagn(ObjectDetailMixin, View):
    model = Tag
    template = 'bank/tag_detail.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_forms = TagForm
    template = 'bank/tag_create.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'bank/post_update.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'bank/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'bank/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'bank/post_delete_form.html'
    redirect_url = 'our_blog'
    raise_exception = True

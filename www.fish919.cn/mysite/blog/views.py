# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html',context={'post_list':post_list})

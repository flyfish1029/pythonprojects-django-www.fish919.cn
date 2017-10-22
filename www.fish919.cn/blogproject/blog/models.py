# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt=models.CharField(max_length=200, blank=True)
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag, blank=True)
	author=models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})

# ureport_website/models.py

from django.db import models


class Partners(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='%Y/%m/%d')
    content = models.TextField()
    website = models.CharField(max_length=255)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UReport Partner'
        verbose_name_plural = 'UReport Partners'


class Read(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='%Y/%m/%d', null=True, blank=True)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UReport Read Article'
        verbose_name_plural = 'UReport Read Articles'


class Watch(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    videourl = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UReport Video'
        verbose_name_plural = 'UReport Videos'


class Quotes(models.Model):
    question = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'UReporter Quote'
        verbose_name_plural = 'UReporter Quotes'

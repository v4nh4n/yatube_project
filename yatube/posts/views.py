from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is index page')


def group_posts(request, slug):
    return HttpResponse('This is group posts page')

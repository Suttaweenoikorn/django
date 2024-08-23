
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def school(request):
    template = loader.get_template('school.html')
    return HttpResponse(template.render())

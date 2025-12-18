from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_view(request):
    return HttpResponse('<h1> HOME PAGE</h1>')

def about_view(request):
    return HttpResponse('<h1> ABOUT US</h1>')

def contact_view(request):
    return HttpResponse('<h1> CONTACT ME</h1>')



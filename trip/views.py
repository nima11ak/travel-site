from django.shortcuts import render


def index_view(request):
    return render(request,'trip/index.html')

def about_view(request):
    return render(request,'trip/about.html')

def contact_view(request):
    return render(request,'trip/contact.html')

def elements_view(request):
    return render(request,'trip/elements.html')

from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context ={'title':'bitcoin crashed again!','context':'bitcoin was flying but now grounded','context2':'bitcoin is bullshit!!','author':'nima ak'}
    return render(request,'blog/blog-single.html',context)
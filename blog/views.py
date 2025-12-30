from django.shortcuts import render, get_object_or_404
from django.db import models
from blog.models import Post

def blog_view(request):
    """
    نمایش لیست همه پست‌های منتشر شده
    """
    posts = Post.objects.filter(status=1)
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    """
    نمایش جزئیات یک پست با قابلیت پست قبلی و بعدی
    """
    # دریافت پست فعلی
    post = get_object_or_404(Post, pk=pid, status=1)
    
    # افزایش تعداد بازدیدها
    Post.objects.filter(pk=pid).update(counted_views=models.F('counted_views') + 1)
    
    # دریافت تمام پست‌های منتشر شده به ترتیب تاریخ (جدیدترین اول)
    all_posts = list(Post.objects.filter(status=1).order_by('-created_date'))
    
    # مقداردهی اولیه متغیرها
    previous_post = None
    next_post = None
    
    # پیدا کردن ایندکس پست فعلی در لیست
    try:
        current_index = all_posts.index(post)
        
        # پست قبلی (ایندکس - 1)
        if current_index > 0:
            previous_post = all_posts[current_index - 1]
        
        # پست بعدی (ایندکس + 1)
        if current_index < len(all_posts) - 1:
            next_post = all_posts[current_index + 1]
            
    except ValueError:
        # اگر پست در لیست پیدا نشد
        pass
    
    # ساخت context
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request,'test.html')
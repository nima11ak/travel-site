from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()


@register.simple_tag(name='totalposts')
def total_posts():
    return Post.objects.filter(status=1).count()


@register.simple_tag(name='posts')
def active_posts():
    return Post.objects.filter(status=1)


@register.filter
def snippet(value):
    return value[:100]


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:5]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts =Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dic = {}
    for name in categories:
        cat_dic[name]=posts.filter(category=name).count()
    return {'categories':cat_dic}


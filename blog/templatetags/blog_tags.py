from django import template
from blog.models import Post

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

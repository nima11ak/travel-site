from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import Truncator


class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/abc.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def excerpt(self, words=5):
        return Truncator(self.body).words(words, truncate='...')

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'
    
    def __str__(self):
        return "{} - {}".format(self.title,self.id)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def get_previous_post(self):
      
        try:
            # پستی که created_date آن بعد از پست فعلی است (ترتیب نزولی)
            return Post.objects.filter(
                created_date__gt=self.created_date,
                status=True  # فقط پست‌های منتشر شده
            ).order_by('created_date').first()
        except Post.DoesNotExist:
            return None
    
    def get_next_post(self):
       
        try:
            # پستی که created_date آن قبل از پست فعلی است (ترتیب نزولی)
            return Post.objects.filter(
                created_date__lt=self.created_date,
                status=True  # فقط پست‌های منتشر شده
            ).order_by('-created_date').first()
        except Post.DoesNotExist:
            return None
        



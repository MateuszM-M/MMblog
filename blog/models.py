from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Article(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
)
    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    post_img =  models.ImageField(null=True, blank=True, upload_to='post_images')
    slug = models.SlugField(max_length=300, 
                            unique=True)
    post_pre_content = models.TextField()
    post_content = RichTextField(blank=True, null=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='Draft')
    created_date = models.DateTimeField(
        auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ('-published_date',)
    
    
    def __str__(self):
        return self.title
    
  
class Comment(models.Model):
    
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=30)
    comment_content = models.TextField(max_length=2000)
    created_date = models.DateTimeField(
        auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created_date',)
        
    def __str__(self):
        return self.comment_content
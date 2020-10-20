from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator



def home(request):
    posts = Article.objects.filter(status='Published')
    paginator = Paginator(posts, 4)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/articles.html', {'posts':posts})


def viewing_post(request, slug):
    comments = Comment.objects.filter(active=True)
    
    
    post = get_object_or_404(Article, slug=slug)
    context = {'post':post, 'comments':comments}
    return render(request, 'blog/viewing_post.html', context)


def about_me(request):
    return render(request, 'blog/about_me.html')


def projects(request):
    return render(request, 'blog/projects.html')


def contact(request):
    return render(request, 'blog/contact.html')

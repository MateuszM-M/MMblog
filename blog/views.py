from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import CommentForm



def home(request):
    posts = Article.objects.filter(status='Published')
    paginator = Paginator(posts, 4)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/articles.html', {'posts':posts})


def viewing_post(request, slug):
    post = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(request.path_info)
    
    context = {'post':post, 'comments':comments,
               'new_comment':new_comment,
                'comment_form':comment_form}
    return render(request, 'blog/viewing_post.html', context)


def about_me(request):
    return render(request, 'blog/about_me.html')


def projects(request):
    return render(request, 'blog/projects.html')


def contact(request):
    return render(request, 'blog/contact.html')

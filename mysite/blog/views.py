from django.shortcuts import render,render_to_response,get_object_or_404
from .models import Blog,BlogType


def index(request):
    return render(request, 'index.html')


def archive(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'frontend/article.html', context)


def tags(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_list'] = BlogType.objects.all()
    return render(request, 'frontend/tags.html', context)


def about(request):
    return render(request, 'frontend/about.html')


def details(request, id):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=id)
    return render_to_response('frontend/details.html', context)





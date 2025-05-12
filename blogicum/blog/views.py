from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post, Category


def index(request):
    """
    Главная страница: 5 последних опубликованных постов
    с проверкой условий публикации
    """
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).select_related('category', 'location', 'author')[:5]
    
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, id):
    """
    Страница отдельного поста с проверкой условий публикации
    """
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    """
    Посты категории с проверкой, что категория опубликована
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).select_related('location', 'author')
  
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })

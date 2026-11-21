from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related(
        'category', 'location', 'author'
    ).order_by('-pub_date')[:5]

    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    ).select_related(
        'category', 'location', 'author'
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)

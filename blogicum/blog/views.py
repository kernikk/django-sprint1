from django.http import Http404
from django.shortcuts import render

posts = [
    ...
]

# Считаем один раз при старте приложения
POSTS_BY_ID = {post['id']: post for post in posts}


def index(request):
    context = {'posts': posts[::-1]}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    try:
        post = POSTS_BY_ID[post_id]
    except KeyError:
        raise Http404('Post not found')

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)

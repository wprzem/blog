from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'pw',
        'title': 'blog post 1',
        'content': 'first content',
        'date_posted': '2021-04-15'
    },
    {
        'author': 'ml',
        'title': 'blog post 2',
        'content': 'second content',
        'date_posted': '2021-04-14'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

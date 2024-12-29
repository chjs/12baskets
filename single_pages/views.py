from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_blog_posts = Post.objects.order_by('-pk')[:4]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_blog_posts': recent_blog_posts,
        }
    )

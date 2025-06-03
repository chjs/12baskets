from django.shortcuts import render
from django.conf import settings
from blog.models import Post


def index(request):
    recent_blog_posts = Post.objects.order_by('-pk')[:4]

    return render(
        request,
        'pages/index.html',
        {
            'kakao_api_key': settings.KAKAO_JS_API_KEY,
            'latitude': settings.LAT,
            'longitude': settings.LNG,
            'recent_blog_posts': recent_blog_posts,
        }
    )

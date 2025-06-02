from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(
        request,
        'pages/index.html',
        {
            'kakao_api_key': settings.KAKAO_JS_API_KEY,
            'latitude': settings.LAT,
            'longitude': settings.LNG,
        }
    )

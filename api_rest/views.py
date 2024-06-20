from django.shortcuts import render
import requests
import json

NEWS_API_KEY = '089f8a09d73f4b32a4ddd6e87cfb8884'

def fetch_news(request):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    content_from_internet = json.loads(response.content)
    context={
    'data':content_from_internet,
    }
    if response.status_code == 200:
        return render(request, 'news.html', context)
    else:
        return render(request, 'news.html', {'error': 'Error'})

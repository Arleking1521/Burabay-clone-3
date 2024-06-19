from django.shortcuts import render
from .models import index_page, openInfo
from news.models import Post, PostAttachment
# Create your views here.

def index(request):
    content = index_page.objects.order_by('-id').first()
    posts = Post.objects.order_by('-date')
    post_list = []
    for post in posts:
        original_content = post.content
        post.content = ' '.join(original_content.split()[:40])
        # Если содержимое было сокращено, добавляем многоточие в конец строки
        if original_content != post.content:
            post.content += ' ...'
        att = PostAttachment.objects.filter(post_id = post.pk).first()
        post_obj = {
            'pk': post.pk if post else None,
            'author': post.author if post else None,
            'title': post.title if post else None,
            'date': post.date if post else None,
            'content': post.content if post else None,
            'att': att if att else None,
        }
        post_list.append(post_obj)
    return render(request, 'MainPage/index.html', {'content': content, "news": post_list})

def site_map(request):
    return render(request, 'MainPage/site_map.html')

def messages(request):
    return render(request, 'MainPage/message.html')

def symbols(request):
    return render(request, 'MainPage/symbols.html')

def OpenInfo(request):
    data = openInfo.objects.order_by('-id').first()
    return render(request, 'infoPages/openInfoDoc.html', {'data' : data})
from django.shortcuts import render, redirect
from mytest.models import Post, Mood

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        mood = Mood.objects.get(status=user_mood)
        post = Post(mood=mood, nickname=user_id, del_pass=user_pass)
    else:
        pass
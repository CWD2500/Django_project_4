from django.shortcuts import render
from WebSitePosts.models import Post
# Create your views here.


def index(request):
    context ={
        'post':Post.objects.all(),
        'last_three_post': Post.objects.all().order_by('-id')[:3],
        'last_four_post': Post.objects.all().order_by('-id')[:4],
        'last_sex_post': Post.objects.all().order_by('-id')[:4],
    }
    return render(request , 'index.html'  , context= context)


def about(request):
    return render(request , 'about.html')


def contact(request):
    return render(request , 'contact.html')


def show(request , pk):
    context ={
        'post':Post.objects.get(pk = pk),
    }

    return render(request , 'show.html' , context=context)
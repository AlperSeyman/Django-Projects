from django.shortcuts import render
from main.models import Post
# Create your views here.

def home_page(request):
    posts = Post.objects.all()
    return render(request, template_name='base.html', context={'title':'Home', 'posts':posts})


def post_page(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, template_name='post_page.html', context={'post':post})
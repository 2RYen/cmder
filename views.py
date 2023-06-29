from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    greeting = "홍길동"
    return render(
        request,
        "blog/index.html",
        {
            "greetings" : greeting
        }
    )


def post_list(request):
    post_list = Post.objects.all()

    return render (
        request,
        'blog/list.html',
        {
            'post_list': post_list,
        }
    )


def post_write1(request):
    if request.method == 'POST':
        # 전송 받은 정보를 테이블 저장
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.writer = request.POST['writer']
        post.save()
        # list로 이동
        return HttpResponseRedirect('/blog/form1/list')

    return render(
        request,
        'blog/write_form1.html',
    )


def post_write2(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.writer = form.cleaned_data['writer']
            post.save()
            return HttpResponseRedirect('/blog/form2/list')

    return render (
        request,
        'blog/write_form2.html',
        {
            'form2': form,
        }
    )




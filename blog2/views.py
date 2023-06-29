from django.shortcuts import render
from .models import Post2
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(
        request,
        "blog2/index.html"
    )


def post2_write(request):
    if request.method == 'POST':
        post = Post2()
        post.subject = request.POST['subject']
        post.content = request.POST['content']
        post.writer = request.POST['writer']
        post.category = request.POST['category']
        post.save()
        return HttpResponseRedirect('/blog2/form1/list')

    return render(
        request,
        "blog2/write_form1.html"
    )



def post2_write_css(request):
    if request.method == 'POST':
        post = Post2()
        post.subject = request.POST['subject']
        post.content = request.POST['content']
        post.writer = request.POST['writer']
        post.category = request.POST['category']
        post.save()
        return HttpResponseRedirect('/blog2/form1/list_css')

    return render(
        request,
        "blog2/write_form1_css.html",
    )


def post2_list(request):
    posts = Post2.objects.all()
    return render(
        request,
        "blog2/list.html",
        {
            'posts':posts,
        }
    )


def post2_list_css(request):
    posts = Post2.objects.all()
    return render(
        request,
        "blog2/list_css.html",
        {
            'posts': posts,
        }
    )
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(
        request,
        "member/index.html"
    )


def list(request):
    members = Member.objects.all()
    return render(
        request,
        "member/memList.html",
        {
            "member_list": members
        }
    )

def css_register(request):
    if request.method == 'POST':
        member = Member()
        member.id = request.POST['id']
        member.name = request.POST['name']
        member.passwd = request.POST['passwd']
        member.gender = request.POST['gender']
        member.hobby = request.POST.getlist('hobby')
        member.job = request.POST['job']
        # member.save()

        try:
            row = Member.objects.get(id=request.POST['id'])
            print("존재 하는 아이디!!!", row.id, row.name)
        except ObjectDoesNotExist:
            member.save()
            return HttpResponseRedirect("/member/css/list")

    return render(
        request,
        "member/memRegForm.html"
    )

def css_list(request):
    members = Member.objects.all()
    return render(
        request,
        "member/memListCss.html",
        {
            "member_list": members
        }
    )














# def css_read(request):
#     if request.method == 'GET':
#         print(request.POST['id'])
#
#     return render(
#         request,
#         "member/memRegForm.html"
#     )
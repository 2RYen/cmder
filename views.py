from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import googletrans


# Create your views here.
def register(request):
    if request.method == "POST":
        person = Person()
        person.id = request.POST['id']
        person.name = request.POST['name']
        person.passwd = request.POST['passwd']
        person.gender = request.POST['gender']
        # person.hobby = request.POST['hobby']
        person.hobby = request.POST.getlist('hobby')
        person.job = request.POST['job']

        try:
            row = Person.objects.get(id=request.POST['id'])
            print("존재하는 아이디 입니다.", row.id, row.name)
        except ObjectDoesNotExist:
            person.save()
            return HttpResponseRedirect('/person/list')

    return render(
        request,
        'person/register.html'
    )


def person_list(request):
    person_list = Person.objects.all()

    return render(
        request,
        'person/list.html',
        {
            'persons': person_list
        }
    )


def update(request):
    if request.method == "GET":
        person = Person.objects.get(id=request.GET['id'])
        return render(
            request,
            'person/update.html',
            {
                'person': person,
            }
        )

    if request.method == "POST":
        person = Person.objects.get(id=request.POST['id'])
        person.id = request.POST['id']
        person.name = request.POST['name']
        person.passwd = request.POST['passwd']
        person.gender = request.POST['gender']
        # person.hobby = request.POST['hobby']
        person.hobby = request.POST.getlist('hobby')
        person.job = request.POST['job']
        person.save()

        return HttpResponseRedirect('/person/list')


def delete(request):
    if request.method == "GET":
        person = Person.objects.get(id=request.GET['id'])
        person.delete()
        return HttpResponseRedirect('/person/list')
    # return render(
    #     request,
    #     "list.html"
    # )


def translate(request):
    if request.method == 'POST':
        input_str = request.POST['src']
        mode = request.POST['mode']

        translator = googletrans.Translator()
        output = translator.translate(input_str, dest=mode)
        return render(
            request,
            'person/translate.html',
            {
                'src': input_str,
                'dest': output.text,
                'mode': mode,
            }
        )

    return render(
        request,
        'person/translate.html',
        {
            'mode': 'en'
        }
    )


import json

import os
import sys
import urllib.request
def translate_papago(request):
    if request.method == 'POST':
        client_id = "uw5y0muAxUqwnlRIrZjO" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "5Z1pLByqJ2" # 개발자센터에서 발급받은 Client Secret 값

        input_str = request.POST['src']
        mode = request.POST['mode']

        encText = urllib.parse.quote("반갑습니다")
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))
            result = json.loads(response_body.decode('utf-8'))
            # print(result['message']['result']['translatedText'])
            output = result['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        # translator = googletrans.Translator()
        # output = translator.translate(input_str, dest=mode)
        return render(
            request,
            'person/translate_papago.html',
            {
                'src': input_str,
                'dest': output.text,
                'mode': mode,
            }
        )

    return render(
        request,
        'person/translate_papago.html',
        {
            'mode': 'en'
        }
    )
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import template
from .models import *


def index(response):
    #b1 = Bd(title='me', content='wowwowwow', price=12345.0).save()
    return HttpResponseRedirect('/cook')


def cook(request):
    bbs = Bd.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric
    }
    return render(request, 'by_rubric.html', context)


def send(request):
    arg1 = str(request.POST.get("title"))
    arg2 = str(request.POST.get("content"))
    arg3 = float(request.POST.get("price"))
    arg4 = str(request.POST.get("rubric_name"))
    Bd(rubric=arg4, title=arg1, content=arg2, price=arg3).save()
    return HttpResponseRedirect('/cook')


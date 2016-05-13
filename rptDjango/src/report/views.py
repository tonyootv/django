# -*- coding: utf-8 -*-
# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from report.models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def index(request):
    return HttpResponse(u"hello word! 欢迎光临！")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

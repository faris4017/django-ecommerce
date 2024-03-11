from django.shortcuts import render

from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request,template_name='home/base.html',context=None)
    
from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'name':'rahul','mobile':'8555968049'}
    return render(request,'jinja2.html',d)
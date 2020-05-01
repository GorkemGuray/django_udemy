from django.shortcuts import render,HttpResponse
from .forms import ArticleForm

def index(request):
    context = {
        "number1":10,
        "number2":20
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request,'about.html')

def dashboard(request):
    return render(request,'dashboard.html')

def addArticle(request):
    form = ArticleForm()
    context = {
        "form":form
    }
    return render (request, 'addarticle.html',context)



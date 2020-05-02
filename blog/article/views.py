from django.shortcuts import render,HttpResponse,redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def dashboard(request):
    article = Article.objects.filter(author=request.user)
    context = {
        "article":article
    }
    return render(request,'dashboard.html',context)

def addArticle(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale başarıyla eklendi.")
        return redirect("index")



    return render (request, 'addarticle.html',{"form":form})

def detail(request,id):
    article = Article.objects.filter(id=id).first()
    return render(request,'detail.html',{"article":article})



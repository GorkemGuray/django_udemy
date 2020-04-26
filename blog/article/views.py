from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        "number1":10,
        "number2":20
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request,'about.html')


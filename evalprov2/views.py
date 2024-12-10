from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "documents.html")


def documentos(request):
    return render(request, "home.html")


def evalprov(request):
    return render(request, "eval.html")

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!!!!")

def sobre(request):
    return HttpResponse("Sobre [..]")

def noticias(request):
    return HttpResponse("noticias [..]")

def autor(request):
    return HttpResponse("Autor [..]")

def empresa(request):
    return HttpResponse("Empresa")
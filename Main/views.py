from django.shortcuts import render
from django.http import HttpResponseNotFound



# Create your views here.
def index (request):
    return render(request, "Main/index.html")


def error_404_demo(request):
    return HttpResponseNotFound(render(request, 'Main/404.html'))
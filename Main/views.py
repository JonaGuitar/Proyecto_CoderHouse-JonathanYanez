from django.shortcuts import render

from functools import wraps
from django.http import HttpResponseNotFound



# Create your views here.
def index (request):
    return render(request, "Main/index.html")


# def error_404_demo(request):
#     return HttpResponseNotFound(render(request, 'Main/404.html'))


def login_required_404(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseNotFound(render(request, 'Main/404.html'))
        return view_func(request, *args, **kwargs)
    return wrapper
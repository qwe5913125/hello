from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello_world!')

def index2(request):
    if request.method == 'GET':
        return render(request, 'my_app/index.html')



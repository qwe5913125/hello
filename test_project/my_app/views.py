from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View

from django.contrib import messages
from django.template import RequestContext

from my_app.forms import MyForm
from my_app.book import MyBook
# Create your views here.


def hello_world(request):
    return HttpResponse('Hello_world!')

def index2(request):
    if request.method == 'GET':
        na = 'ivn'
        return render(request, 'my_app/index.html', {'name': na})


class MyView(View):
    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'my_app/form.html', c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'Validation failed')

        c = {'form': form}
        return render(request, 'my_app/form.html', c)


class MyViewBook(View):
    def get(self, request):
        form = MyBook()
        c = {'form': form}
        return render(request, 'my_app/book.html', c)

    def post(self, request):
        form = MyBook(data=request.POST)

        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
            messages.success(request, form.cleaned_data['name'])
        else:
            messages.error(request, 'Validation failed')




        c = {'form': form}
        return render(request, 'my_app/book.html', c)

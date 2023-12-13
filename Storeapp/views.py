from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader


def storeapp(request):
    html_template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(html_template.render(context, request))

# def index(request):
#     template_model = {
#         "name": "Popescu",
#         "address": "Timisoara, Parcul Rozelor"
#     }
#     return render(request, "home/home.html", template_model)

def example_view(request):
    return render(request, 'Storeapp/example.html')



def home(request):
    return render(request, 'home/home.html')

from django.shortcuts import render


def index(request):
    template_model = {
        "name": "Popescu",
        "address": "Timisoara, Parcul Rozelor"
    }
    return render(request, "home/home.html", template_model)

def example_view(request):
    return render(request, 'Storeapp/example.html')



def home(request):
    return render(request, 'home/home.html')

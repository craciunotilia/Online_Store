from django.shortcuts import render


def index(request):
    template_model = {
        "name": "Popescu",
        "address": "Timisoara, Parcul Rozelor"
    }
    return render(request, "index.html", template_model)

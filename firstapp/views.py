from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Спасибо! Я вам перезвоню</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


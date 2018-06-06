from django.shortcuts import render, redirect
from django.contrib.auth import logout
from cadastro.models import CadProd


def home(request):
    produtos = CadProd.objects.all()
    print(produtos)
    return render(request, 'home.html', {'produtos':produtos})


def my_logout(request):
    logout(request)

    return redirect('home')

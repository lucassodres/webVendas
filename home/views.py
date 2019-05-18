from __future__ import unicode_literals
from django.shortcuts import render
from cadastros.usuarios.models import Usuarios
from estoque.produtos.models import Produtos, ImagensProdutos
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')

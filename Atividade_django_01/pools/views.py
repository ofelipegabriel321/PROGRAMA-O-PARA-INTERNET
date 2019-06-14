from django.shortcuts import render
from pools.templates import *


def index(request):
    return render(request, 'index.html')

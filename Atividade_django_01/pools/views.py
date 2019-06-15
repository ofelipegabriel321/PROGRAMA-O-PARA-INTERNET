from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def question(request, id_question):
    question_rendered = Question.objects.get(id=id_question)
    data = {'question': question_rendered}

    return render(request, 'question.html', data)

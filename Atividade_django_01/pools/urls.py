from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('question/<int:id_question>/', question)
]

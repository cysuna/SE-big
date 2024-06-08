from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

from django.http import HttpResponse
from django.shortcuts import render

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
def home(request):
    return render(request, 'home.html')
def questions(request):
    return render(request, 'questions.html')
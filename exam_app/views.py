from rest_framework import viewsets
from .models import Question, Exam
from .serializers import QuestionSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExamForm
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
def home(request):
    return render(request, 'home.html')
def questions(request):
    return render(request, 'questions.html')

def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        questions_data = [
            {
                "id": question.id,
                "question_text": question.question_text,
                "question_type": question.question_type,
                "difficulty": question.difficulty,
                "answer": question.answer
            }
            for question in questions
        ]
        return JsonResponse(questions_data, safe=False)
    
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})

def do_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, 'do_exam.html', {'exam': exam})

def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'create_exam.html', {'form': form})
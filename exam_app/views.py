from rest_framework import viewsets
from .models import Exam, SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion
from .serializers import SingleChoiceQuestionSerializer, MultipleChoiceQuestionSerializer, TrueFalseQuestionSerializer, ShortAnswerQuestionSerializer, ExamSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExamForm
from django.contrib.auth.decorators import login_required
from .forms import SingleChoiceQuestionForm, MultipleChoiceQuestionForm, TrueFalseQuestionForm, ShortAnswerQuestionForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
    
def home(request):
    return render(request, 'home.html')
def questions(request):
    return render(request, 'questions.html')

@api_view(['GET'])
def question_list(request):
    if request.method == 'GET':
        single_choice_questions = SingleChoiceQuestion.objects.all()
        multiple_choice_questions = MultipleChoiceQuestion.objects.all()
        true_false_questions = TrueFalseQuestion.objects.all()
        short_answer_questions = ShortAnswerQuestion.objects.all()

        single_choice_serializer = SingleChoiceQuestionSerializer(single_choice_questions, many=True)
        multiple_choice_serializer = MultipleChoiceQuestionSerializer(multiple_choice_questions, many=True)
        true_false_serializer = TrueFalseQuestionSerializer(true_false_questions, many=True)
        short_answer_serializer = ShortAnswerQuestionSerializer(short_answer_questions, many=True)

        questions_data = {
            "single_choice_questions": single_choice_serializer.data,
            "multiple_choice_questions": multiple_choice_serializer.data,
            "true_false_questions": true_false_serializer.data,
            "short_answer_questions": short_answer_serializer.data
        }

        return Response(questions_data)
    
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

def select_question_type(request):
    if request.method == 'POST':
        question_type = request.POST.get('question_type')
        if question_type == 'single_choice':
            return redirect('create_single_choice_question')
        elif question_type == 'multiple_choice':
            return redirect('create_multiple_choice_question')
        elif question_type == 'true_false':
            return redirect('create_true_false_question')
        elif question_type == 'short_answer':
            return redirect('create_short_answer_question')
    return render(request, 'select_question_type.html')

@login_required
def create_single_choice_question(request):
    if request.method == 'POST':
        form = SingleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user  # 设置 created_by 字段
            question.save()
            return redirect('teacher_home')
    else:
        form = SingleChoiceQuestionForm()
    return render(request, 'create_single_choice_question.html', {'form': form})

@login_required
def create_multiple_choice_question(request):
    if request.method == 'POST':
        form = MultipleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user  # 设置 created_by 字段
            question.save()
            return redirect('teacher_home')
    else:
        form = MultipleChoiceQuestionForm()
    return render(request, 'create_multiple_choice_question.html', {'form': form})

@login_required
def create_true_false_question(request):
    if request.method == 'POST':
        form = TrueFalseQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user  # 设置 created_by 字段
            question.save()
            return redirect('teacher_home')
    else:
        form = TrueFalseQuestionForm()
    return render(request, 'create_true_false_question.html', {'form': form})

@login_required
def create_short_answer_question(request):
    if request.method == 'POST':
        form = ShortAnswerQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user  # 设置 created_by 字段
            question.save()
            return redirect('teacher_home')
    else:
        form = ShortAnswerQuestionForm()
    return render(request, 'create_short_answer_question.html', {'form': form})

class SingleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = SingleChoiceQuestion.objects.all()
    serializer_class = SingleChoiceQuestionSerializer

class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer

class TrueFalseQuestionViewSet(viewsets.ModelViewSet):
    queryset = TrueFalseQuestion.objects.all()
    serializer_class = TrueFalseQuestionSerializer

class ShortAnswerQuestionViewSet(viewsets.ModelViewSet):
    queryset = ShortAnswerQuestion.objects.all()
    serializer_class = ShortAnswerQuestionSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
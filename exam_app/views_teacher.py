from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Exam
from .forms import QuestionForm, ExamForm
@login_required
def teacher_home(request):
    if not request.user.groups.filter(name='Teachers').exists():
        return redirect('home')

    questions = Question.objects.filter(created_by=request.user)
    return render(request, 'teacher_home.html', {'questions': questions})
@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('teacher_home')
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})

@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id, created_by=request.user)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'edit_question.html', {'form': form})

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id, created_by=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('teacher_home')
    return render(request, 'delete_question.html', {'question': question})

@login_required
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')
    else:
        form = ExamForm()
    return render(request, 'create_exam.html', {'form': form})
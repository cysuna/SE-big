from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Question

class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type', 'difficulty', 'answer']

@login_required
def admin_home(request):
    if not request.user.is_staff:
        return redirect('home')
    
    teachers = User.objects.filter(groups__name='Teachers')
    questions = Question.objects.all()
    return render(request, 'admin_home.html', {'teachers': teachers, 'questions': questions})

@login_required
def add_teacher(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            teacher_group, created = Group.objects.get_or_create(name='Teachers')
            teacher.groups.add(teacher_group)
            return redirect('admin_home')
    else:
        form = TeacherForm()
    
    return render(request, 'add_teacher.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            student_group, created = Group.objects.get_or_create(name='Students')
            student.groups.add(student_group)
            return redirect('home')
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})

@login_required
def edit_teacher(request, teacher_id):
    if not request.user.is_staff:
        return redirect('home')
    
    teacher = get_object_or_404(User, pk=teacher_id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'edit_teacher.html', {'form': form})

@login_required
def delete_teacher(request, teacher_id):
    if not request.user.is_staff:
        return redirect('home')
    
    teacher = get_object_or_404(User, pk=teacher_id)
    teacher.delete()
    return redirect('admin_home')

@login_required
def add_question(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = QuestionForm()
    
    return render(request, 'add_question.html', {'form': form})

@login_required
def edit_question(request, question_id):
    if not request.user.is_staff:
        return redirect('home')
    
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'edit_question.html', {'form': form})

@login_required
def delete_question(request, question_id):
    if not request.user.is_staff:
        return redirect('home')
    
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('admin_home')

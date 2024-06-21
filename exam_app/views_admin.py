from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion, Exam
from .forms import ExamForm, SingleChoiceQuestionForm, MultipleChoiceQuestionForm, TrueFalseQuestionForm, ShortAnswerQuestionForm
from collections import Counter

# 用户注册表单
class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

@login_required
def admin_home(request):
    if not request.user.is_staff:
        return redirect('home')
    
    teachers = User.objects.filter(groups__name='Teachers')
    students = User.objects.filter(groups__name='Students')
    exams = Exam.objects.all()
    single_choice_questions = SingleChoiceQuestion.objects.all()
    multiple_choice_questions = MultipleChoiceQuestion.objects.all()
    true_false_questions = TrueFalseQuestion.objects.all()
    short_answer_questions = ShortAnswerQuestion.objects.all()
    
    context = {
        'teachers': teachers,
        'students': students,
        'exams': exams,
        'single_choice_questions': single_choice_questions,
        'multiple_choice_questions': multiple_choice_questions,
        'true_false_questions': true_false_questions,
        'short_answer_questions': short_answer_questions
    }
    
    return render(request, 'admin_home.html', context)
# 添加教师
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

# 编辑教师
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

# 删除教师
@login_required
def delete_teacher(request, teacher_id):
    if not request.user.is_staff:
        return redirect('home')
    
    teacher = get_object_or_404(User, pk=teacher_id)
    teacher.delete()
    return redirect('admin_home')

# 添加学生
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

# 添加单选题
@login_required
def add_single_choice_question(request):
    if request.method == 'POST':
        form = SingleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('admin_home')
    else:
        form = SingleChoiceQuestionForm()
    return render(request, 'create_single_choice_question.html', {'form': form})

@login_required
def add_multiple_choice_question(request):
    if request.method == 'POST':
        form = MultipleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('admin_home')
    else:
        form = MultipleChoiceQuestionForm()
    return render(request, 'create_multiple_choice_question.html', {'form': form})

@login_required
def add_true_false_question(request):
    if request.method == 'POST':
        form = TrueFalseQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('admin_home')
    else:
        form = TrueFalseQuestionForm()
    return render(request, 'create_true_false_question.html', {'form': form})

@login_required
def add_short_answer_question(request):
    if request.method == 'POST':
        form = ShortAnswerQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('admin_home')
    else:
        form = ShortAnswerQuestionForm()
    return render(request, 'create_short_answer_question.html', {'form': form})

@login_required
def edit_question(request, question_id, question_type):
    if question_type == 'single_choice':
        question = get_object_or_404(SingleChoiceQuestion, id=question_id, created_by=request.user)
        form_class = SingleChoiceQuestionForm
    elif question_type == 'multiple_choice':
        question = get_object_or_404(MultipleChoiceQuestion, id=question_id, created_by=request.user)
        form_class = MultipleChoiceQuestionForm
    elif question_type == 'true_false':
        question = get_object_or_404(TrueFalseQuestion, id=question_id, created_by=request.user)
        form_class = TrueFalseQuestionForm
    elif question_type == 'short_answer':
        question = get_object_or_404(ShortAnswerQuestion, id=question_id, created_by=request.user)
        form_class = ShortAnswerQuestionForm
    else:
        return redirect('admin_home')

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = form_class(instance=question)
    return render(request, 'edit_question.html', {'form': form})

@login_required
def delete_question(request, question_id, question_type):
    if question_type == 'single_choice':
        question = get_object_or_404(SingleChoiceQuestion, id=question_id, created_by=request.user)
    elif question_type == 'multiple_choice':
        question = get_object_or_404(MultipleChoiceQuestion, id=question_id, created_by=request.user)
    elif question_type == 'true_false':
        question = get_object_or_404(TrueFalseQuestion, id=question_id, created_by=request.user)
    elif question_type == 'short_answer':
        question = get_object_or_404(ShortAnswerQuestion, id=question_id, created_by=request.user)
    else:
        return redirect('admin_home')

    if request.method == 'POST':
        question.delete()
        return redirect('admin_home')
    return render(request, 'delete_question.html', {'question': question, 'question_type': question_type})

# 添加试卷
@login_required
def add_exam(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ExamForm()
        print(form.errors)  # 打印表单错误信息
    
    return render(request, 'create_exam.html', {'form': form})

# 编辑试卷
@login_required
def edit_exam(request, exam_id):
    if not request.user.is_staff:
        return redirect('home')
    
    exam = get_object_or_404(Exam, id=exam_id)
    
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ExamForm(instance=exam)
    
    # 收集题目类型和难度的数据
    single_choice_count = exam.single_choice_questions.count()
    multiple_choice_count = exam.multiple_choice_questions.count()
    true_false_count = exam.true_false_questions.count()
    short_answer_count = exam.short_answer_questions.count()

    difficulty_counter = Counter()
    for question in exam.single_choice_questions.all():
        difficulty_counter[question.difficulty] += 1
    for question in exam.multiple_choice_questions.all():
        difficulty_counter[question.difficulty] += 1
    for question in exam.true_false_questions.all():
        difficulty_counter[question.difficulty] += 1
    for question in exam.short_answer_questions.all():
        difficulty_counter[question.difficulty] += 1

    context = {
        'form': form,
        'single_choice_count': single_choice_count,
        'multiple_choice_count': multiple_choice_count,
        'true_false_count': true_false_count,
        'short_answer_count': short_answer_count,
        'difficulty_counter': dict(difficulty_counter)  # 转换为字典以便在模板中使用
    }
    
    return render(request, 'edit_exam.html', context)

# 删除试卷
@login_required
def delete_exam(request, exam_id):
    if not request.user.is_staff:
        return redirect('home')
    
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    return redirect('admin_home')

@login_required
def choose_question_type(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'choose_question_type_admin.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exam, SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion
from .forms import SingleChoiceQuestionForm, MultipleChoiceQuestionForm, TrueFalseQuestionForm, ShortAnswerQuestionForm, ExamForm

@login_required
def teacher_home(request):
    if not request.user.groups.filter(name='Teachers').exists():
        return redirect('home')

    single_choice_questions = SingleChoiceQuestion.objects.filter(created_by=request.user)
    multiple_choice_questions = MultipleChoiceQuestion.objects.filter(created_by=request.user)
    true_false_questions = TrueFalseQuestion.objects.filter(created_by=request.user)
    short_answer_questions = ShortAnswerQuestion.objects.filter(created_by=request.user)

    context = {
        'single_choice_questions': single_choice_questions,
        'multiple_choice_questions': multiple_choice_questions,
        'true_false_questions': true_false_questions,
        'short_answer_questions': short_answer_questions,
    }
    return render(request, 'teacher_home.html', context)

@login_required
def create_question(request):
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
    return render(request, 'choose_question_type.html')

@login_required
def create_single_choice_question(request):
    if request.method == 'POST':
        form = SingleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
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
            question.created_by = request.user
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
            question.created_by = request.user
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
            question.created_by = request.user
            question.save()
            return redirect('teacher_home')
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
        return redirect('teacher_home')

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')
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
        return redirect('teacher_home')

    if request.method == 'POST':
        question.delete()
        return redirect('teacher_home')
    return render(request, 'delete_question.html', {'question': question, 'question_type': question_type})

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
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Exam
# from .forms import QuestionForm, ExamForm
# @login_required
# def teacher_home(request):
#     if not request.user.groups.filter(name='Teachers').exists():
#         return redirect('home')

#     questions = Question.objects.filter(created_by=request.user)
#     return render(request, 'teacher_home.html', {'questions': questions})
# @login_required
# def create_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.created_by = request.user
#             question.save()
#             return redirect('teacher_home')
#     else:
#         form = QuestionForm()
#     return render(request, 'create_question.html', {'form': form})

# @login_required
# def edit_question(request, question_id):
#     question = get_object_or_404(Question, id=question_id, created_by=request.user)
#     if request.method == 'POST':
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_home')
#     else:
#         form = QuestionForm(instance=question)
#     return render(request, 'edit_question.html', {'form': form})

# @login_required
# def delete_question(request, question_id):
#     question = get_object_or_404(Question, id=question_id, created_by=request.user)
#     if request.method == 'POST':
#         question.delete()
#         return redirect('teacher_home')
#     return render(request, 'delete_question.html', {'question': question})

# @login_required
# def create_exam(request):
#     if request.method == 'POST':
#         form = ExamForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_home')
#     else:
#         form = ExamForm()
#     return render(request, 'create_exam.html', {'form': form})
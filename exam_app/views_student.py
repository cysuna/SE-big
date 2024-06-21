from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Exam

@login_required
def student_home(request):
    exams = Exam.objects.all()
    return render(request, 'student_home.html', {'exams': exams})

@login_required
def do_exam(request, exam_id=None):
    if exam_id == 0:
        exam_id = request.GET.get('exam_id')
    exam = get_object_or_404(Exam, id=exam_id)
    
    if request.method == 'POST':
        total_questions = (exam.single_choice_questions.count() +
                           exam.multiple_choice_questions.count() +
                           exam.true_false_questions.count() +
                           exam.short_answer_questions.count())
        correct_answers = 0
        
        for question in exam.single_choice_questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer is not None:
                correct_answer = ["choice1", "choice2", "choice3", "choice4"][question.correct_choice]
                if user_answer.lower() == correct_answer.lower():
                    correct_answers += 1

        for question in exam.multiple_choice_questions.all():
            user_choices = request.POST.getlist(f'question_{question.id}')
            correct_choices_indices = question.correct_choices
            correct_choices = ["choice1", "choice2", "choice3", "choice4"]
            correct_choices = [correct_choices[int(choice)] for choice in correct_choices_indices]
            if set(user_choices) == set(correct_choices):
                correct_answers += 1

        for question in exam.true_false_questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer is not None and user_answer.lower() == str(question.correct_answer).lower():
                correct_answers += 1

        for question in exam.short_answer_questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer is not None and user_answer.lower() == question.answer.lower():
                correct_answers += 1

        score = (correct_answers / total_questions) * 100
        return redirect('exam_result', score=round(score, 2))
    
    context = {
        'exam': exam,
        'single_choice_questions': exam.single_choice_questions.all(),
        'multiple_choice_questions': exam.multiple_choice_questions.all(),
        'true_false_questions': exam.true_false_questions.all(),
        'short_answer_questions': exam.short_answer_questions.all()
    }
    
    return render(request, 'do_exam.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def exam_result(request, score):
    return render(request, 'exam_result.html', {'score': score})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Exam, Question

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
        total_questions = exam.questions.count()
        correct_answers = 0
        for question in exam.questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer is not None:
                if question.question_type == 'single_choice':
                    if user_answer.lower() == question.answer.lower():
                        correct_answers += 1
                elif question.question_type == 'multiple_choice':
                    user_choices = request.POST.getlist(f'question_{question.id}')
                    if set(user_choices) == set(question.correct_choices):
                        correct_answers += 1
                elif question.question_type == 'true_false':
                    if user_answer.lower() == question.answer.lower():
                        correct_answers += 1
                elif question.question_type == 'short_answer':
                    if user_answer.lower() == question.answer.lower():
                        correct_answers += 1
                else:
                    print(f'Unknown question type for question ID {question.id}')
            else:
                print(f'User answer for question ID {question.id} is None')
        score = (correct_answers / total_questions) * 100
        return redirect('exam_result', score=round(score, 2))
    return render(request, 'do_exam.html', {'exam': exam})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def exam_result(request, score):
    return render(request, 'exam_result.html', {'score': score})
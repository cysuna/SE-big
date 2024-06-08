from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question

@login_required
def teacher_home(request):
    if not request.user.groups.filter(name='Teachers').exists():
        return redirect('home')
    
    questions = Question.objects.filter(created_by=request.user)
    return render(request, 'teacher_home.html', {'questions': questions})

from django import forms
from .models import Question,Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'questions']
        widgets = {
            'questions': forms.CheckboxSelectMultiple,
        }
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type', 'difficulty', 'answer']

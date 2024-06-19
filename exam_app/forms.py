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
        fields = ['question_text', 'question_type', 'choice1', 'choice2', 'choice3', 'choice4', 'true_false' , 'correct_choices', 'answer', 'difficulty']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 2}),
            'question_type': forms.Select(attrs={'id': 'id_question_type'}),
            'choice1': forms.TextInput(attrs={'id': 'id_choice1'}),
            'choice2': forms.TextInput(attrs={'id': 'id_choice2'}),
            'choice3': forms.TextInput(attrs={'id': 'id_choice3'}),
            'choice4': forms.TextInput(attrs={'id': 'id_choice4'}),
            'true_false': forms.CheckboxSelectMultiple(attrs={'id': 'id_true_false'}),
            'correct_choices': forms.CheckboxSelectMultiple(attrs={'id': 'id_correct_choices'}),
            'answer': forms.TextInput(attrs={'id': 'id_answer'}),
        }
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        question_type = self.instance.question_type if self.instance else 'short_answer'
        if question_type in ['single_choice', 'multiple_choice']:

            # self.fields['true_false'].widget = forms.HiddenInput()
        elif question_type == 'true_false':
            self.widget['answer'] = forms.Select(choices=[('true', 'True'), ('false', 'False')])
            self.widget['correct_choices'] = forms.HiddenInput()
            self.widget['choice1'] = forms.HiddenInput()
            self.widget['choice2'] = forms.HiddenInput()
            self.widget['choice3'] = forms.HiddenInput()
            self.widget['choice4'] = forms.HiddenInput()
        elif question_type == 'short_answer':
            self.widget['correct_choices'] = forms.HiddenInput()
            self.widget['choice1'] = forms.HiddenInput()
            self.widget['choice2'] = forms.HiddenInput()
            self.widget['choice3'] = forms.HiddenInput()
            self.widget['choice4'] = forms.HiddenInput()
            # self.fields['true_false'].widget = forms.HiddenInput()

        else:
            self.widget['correct_choices'] = forms.CheckboxSelectMultiple(choices=[
                ('choice1', 'Choice 1'),
                ('choice2', 'Choice 2'),
                ('choice3', 'Choice 3'),
                ('choice4', 'Choice 4'),
            ])
            self.widget['true_false'] = forms.CheckboxSelectMultiple(choices=[
                ('true', 'true'),
                ('false', 'false'),
            ])
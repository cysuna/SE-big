from django import forms
from .models import Exam, SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'single_choice_questions', 'multiple_choice_questions', 'true_false_questions', 'short_answer_questions']
        widgets = {
            'single_choice_questions': forms.CheckboxSelectMultiple,
            'multiple_choice_questions': forms.CheckboxSelectMultiple,
            'true_false_questions': forms.CheckboxSelectMultiple,
            'short_answer_questions': forms.CheckboxSelectMultiple,
        }

# class SingleChoiceQuestionForm(forms.ModelForm):
#     class Meta:
#         model = SingleChoiceQuestion
#         fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice', 'difficulty']
#         widgets = {
#             'question_text': forms.Textarea(attrs={'rows': 2}),
#             'choice1': forms.TextInput(attrs={'placeholder': 'Choice 1'}),
#             'choice2': forms.TextInput(attrs={'placeholder': 'Choice 2'}),
#             'choice3': forms.TextInput(attrs={'placeholder': 'Choice 3'}),
#             'choice4': forms.TextInput(attrs={'placeholder': 'Choice 4'}),
#             'correct_choice': forms.Select(attrs={'placeholder': 'Correct Choice'}),
#         }

# class MultipleChoiceQuestionForm(forms.ModelForm):
#     class Meta:
#         model = MultipleChoiceQuestion
#         fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choices', 'difficulty']
#         widgets = {
#             'question_text': forms.Textarea(attrs={'rows': 2}),
#             'choice1': forms.TextInput(attrs={'placeholder': 'Choice 1'}),
#             'choice2': forms.TextInput(attrs={'placeholder': 'Choice 2'}),
#             'choice3': forms.TextInput(attrs={'placeholder': 'Choice 3'}),
#             'choice4': forms.TextInput(attrs={'placeholder': 'Choice 4'}),
#             'correct_choices': forms.CheckboxSelectMultiple(),
#         }

# class TrueFalseQuestionForm(forms.ModelForm):
#     class Meta:
#         model = TrueFalseQuestion
#         fields = ['question_text', 'correct_answer', 'difficulty']
#         widgets = {
#             'question_text': forms.Textarea(attrs={'rows': 2}),
#             'correct_answer': forms.Select(choices=[('true', 'True'), ('false', 'False')]),
#         }

# class ShortAnswerQuestionForm(forms.ModelForm):
#     class Meta:
#         model = ShortAnswerQuestion
#         fields = ['question_text', 'answer', 'difficulty']
#         widgets = {
#             'question_text': forms.Textarea(attrs={'rows': 2}),
#             'answer': forms.Textarea(attrs={'rows': 2}),
#         }

class SingleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = SingleChoiceQuestion
        fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice', 'difficulty']
        widgets = {
            'correct_choice': forms.RadioSelect(choices=[
                (0, 'choice1'),
                (1, 'choice2'),
                (2, 'choice3'),
                (3, 'choice4')
            ])
        }

class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choices', 'difficulty']
        widgets = {
            'correct_choices': forms.CheckboxSelectMultiple(choices=[
                (0, 'choice1'),
                (1, 'choice2'),
                (2, 'choice3'),
                (3, 'choice4')
            ])
        }

class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = TrueFalseQuestion
        fields = ['question_text', 'correct_answer', 'difficulty']

class ShortAnswerQuestionForm(forms.ModelForm):
    class Meta:
        model = ShortAnswerQuestion
        fields = ['question_text', 'answer', 'difficulty']
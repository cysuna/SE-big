# from django.db import models

# class Question(models.Model):
#     QUESTION_TYPES = (
#         ('MCQ', 'Multiple Choice Question'),
#         ('TF', 'True/False'),
#         ('SA', 'Short Answer'),
#     )

#     question_text = models.CharField(max_length=200)
#     question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
#     difficulty = models.IntegerField()

#     def __str__(self):
#         return self.question_text
from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    QUESTION_TYPES = (
        ('single_choice', 'Single Choice'),
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer'),
    )

    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    choice1 = models.CharField(max_length=200, blank=True, null=True)
    choice2 = models.CharField(max_length=200, blank=True, null=True)
    choice3 = models.CharField(max_length=200, blank=True, null=True)
    choice4 = models.CharField(max_length=200, blank=True, null=True)
    true_false = models.JSONField(blank=True, null=True)
    correct_choices = models.JSONField(blank=True, null=True)  # Store correct choices for multiple choice questions
    answer = models.CharField(max_length=200, blank=True, null=True)  # For True/False and Short Answer
    difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text
    
class Exam(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

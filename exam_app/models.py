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
        ('single', '单选题'),
        ('multiple', '多选题'),
        ('true_false', '判断题'),
        ('short_answer', '问答题'),
    )

    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    difficulty = models.IntegerField()
    answer = models.TextField(default='')  # 确保这一行存在
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text
    
class Exam(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

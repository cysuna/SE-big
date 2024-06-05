from django.db import models

class Question(models.Model):
    QUESTION_TYPES = (
        ('MCQ', 'Multiple Choice Question'),
        ('TF', 'True/False'),
        ('SA', 'Short Answer'),
    )

    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.question_text

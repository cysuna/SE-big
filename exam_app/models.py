from django.db import models
from django.contrib.auth.models import User

class SingleChoiceQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct_choice = models.IntegerField()  # Store index of the correct choice (0-3)
    difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class MultipleChoiceQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct_choices = models.JSONField()  # Store a list of correct choices
    difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class TrueFalseQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField()
    difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class ShortAnswerQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.TextField()
    difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Exam(models.Model):
    title = models.CharField(max_length=255)
    single_choice_questions = models.ManyToManyField(SingleChoiceQuestion, blank=True)
    multiple_choice_questions = models.ManyToManyField(MultipleChoiceQuestion, blank=True)
    true_false_questions = models.ManyToManyField(TrueFalseQuestion, blank=True)
    short_answer_questions = models.ManyToManyField(ShortAnswerQuestion, blank=True)

    def __str__(self):
        return self.title
# from django.db import models
# from django.contrib.auth.models import User

# class SingleChoiceQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     choice1 = models.CharField(max_length=200)
#     choice2 = models.CharField(max_length=200)
#     choice3 = models.CharField(max_length=200)
#     choice4 = models.CharField(max_length=200)
#     correct_choice = models.CharField(max_length=200)
#     difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
#     created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question_text

# class MultipleChoiceQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     choice1 = models.CharField(max_length=200)
#     choice2 = models.CharField(max_length=200)
#     choice3 = models.CharField(max_length=200)
#     choice4 = models.CharField(max_length=200)
#     correct_choices = models.JSONField()  # Store a list of correct choices
#     difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
#     created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question_text

# class TrueFalseQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     correct_answer = models.BooleanField()
#     difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
#     created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question_text

# class ShortAnswerQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     answer = models.TextField()
#     difficulty = models.CharField(max_length=10, choices=(('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')))
#     created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question_text

# class Exam(models.Model):
#     title = models.CharField(max_length=255)
#     single_choice_questions = models.ManyToManyField(SingleChoiceQuestion, blank=True)
#     multiple_choice_questions = models.ManyToManyField(MultipleChoiceQuestion, blank=True)
#     true_false_questions = models.ManyToManyField(TrueFalseQuestion, blank=True)
#     short_answer_questions = models.ManyToManyField(ShortAnswerQuestion, blank=True)

#     def __str__(self):
#         return self.title
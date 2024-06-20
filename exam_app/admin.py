# from django.contrib import admin
# from .models import Question
# from .models import Exam

# admin.site.register(Question)
# admin.site.register(Exam)
from django.contrib import admin
from .models import SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion, Exam

admin.site.register(SingleChoiceQuestion)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(TrueFalseQuestion)
admin.site.register(ShortAnswerQuestion)
admin.site.register(Exam)
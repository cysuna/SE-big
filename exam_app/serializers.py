# from rest_framework import serializers
# from .models import Question

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = '__all__'
from rest_framework import serializers
from .models import SingleChoiceQuestion, MultipleChoiceQuestion, TrueFalseQuestion, ShortAnswerQuestion, Exam

class SingleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceQuestion
        fields = '__all__'

class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'

class TrueFalseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueFalseQuestion
        fields = '__all__'

class ShortAnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortAnswerQuestion
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    single_choice_questions = SingleChoiceQuestionSerializer(many=True)
    multiple_choice_questions = MultipleChoiceQuestionSerializer(many=True)
    true_false_questions = TrueFalseQuestionSerializer(many=True)
    short_answer_questions = ShortAnswerQuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'
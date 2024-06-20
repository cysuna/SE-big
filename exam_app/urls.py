# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import QuestionViewSet , questions
# from .views_auth import login, teacher_login, admin_login
# from .views import home
# from .views_teacher import teacher_home
# from .views_admin import admin_home

# router = DefaultRouter()
# router.register(r'questions', QuestionViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('login/', login, name='login'),
#     path('', home, name='home'),
#     path('questions/', questions, name='questions'),
#     path('teacher/', teacher_home, name='teacher_home'),
#     path('teacher_login/', teacher_login, name='teacher_login'),
#     path('admin_login/', admin_login, name='admin_login'),
#     path('admin_home/', admin_home, name='admin_home'), 
# ]

from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import exam_list, do_exam, create_exam,\
    select_question_type, create_multiple_choice_question, create_true_false_question, \
    create_single_choice_question, create_short_answer_question, \
    SingleChoiceQuestionViewSet, MultipleChoiceQuestionViewSet, TrueFalseQuestionViewSet, ShortAnswerQuestionViewSet, ExamViewSet
from .views_auth import login, teacher_login, admin_login
from .views_teacher import teacher_home, create_question, edit_question, delete_question, create_exam
from .views_admin import (
    admin_home,
    add_teacher, edit_teacher, delete_teacher,
    add_student,
    add_single_choice_question, add_multiple_choice_question, add_true_false_question, add_short_answer_question,
    edit_question, delete_question,
    add_exam, edit_exam, delete_exam 
)
from .views_student import student_home, do_exam, logout_view, exam_result
from .views_admin import (
    admin_home, add_teacher, edit_teacher, delete_teacher,
    add_student, add_single_choice_question, add_multiple_choice_question,
    add_true_false_question, add_short_answer_question, edit_question, 
    delete_question, add_exam, edit_exam, delete_exam
)
router = DefaultRouter()
router.register(r'single_choice_questions', SingleChoiceQuestionViewSet)
router.register(r'multiple_choice_questions', MultipleChoiceQuestionViewSet)
router.register(r'true_false_questions', TrueFalseQuestionViewSet)
router.register(r'short_answer_questions', ShortAnswerQuestionViewSet)
router.register(r'exams', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    path('teacher_login/', teacher_login, name='teacher_login'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('admin_login/', admin_login, name='admin_login'),
    # path('login/admin/', admin_home, name='admin_home'),
    # path('admin/add_question/', add_question, name='add_question'),
    path('admin/', admin_home, name='admin_home'),
    path('admin/add_teacher/', add_teacher, name='add_teacher'),
    path('admin/edit_teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('admin/delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    # path('admin/add_student/', add_student, name='add_student'),
    path('admin/add_single_choice_question/', add_single_choice_question, name='add_single_choice_question'),
    path('admin/add_multiple_choice_question/', add_multiple_choice_question, name='add_multiple_choice_question'),
    path('admin/add_true_false_question/', add_true_false_question, name='add_true_false_question'),
    path('admin/add_short_answer_question/', add_short_answer_question, name='add_short_answer_question'),
    path('admin/edit_question/<int:question_id>/', edit_question, name='edit_question'),
    path('admin/delete_question/<int:question_id>/', delete_question, name='delete_question'),
    path('admin/add_exam/', add_exam, name='add_exam'),
    path('admin/edit_exam/int:exam_id/', edit_exam, name='edit_exam'),
    path('admin/delete_exam/int:exam_id/', delete_exam, name='delete_exam'),
    # path('questions/', questions, name='questions'),
    # path('login/questions/', question_list, name='question_list'),
    # path('do_exam/', do_exam, name='do_exam'), 
    path('do_exam/<int:exam_id>/', do_exam, name='do_exam'),
    path('create_exam/', create_exam, name='create_exam'),
    path('exams/', exam_list, name='exam_list'),  # 添加试卷列表的URL
    path('teacher/', teacher_home, name='teacher_home'),
    path('teacher/create_question/', create_question, name='create_question'),
    path('teacher/edit_question/<int:question_id>/<str:question_type>/', edit_question, name='edit_question'),
    path('teacher/delete_question/<int:question_id>/<str:question_type>/', delete_question, name='delete_question'),
    path('teacher/create_exam/', create_exam, name='create_exam'),
    path('student/', student_home, name='student_home'),
    path('student/do_exam/', do_exam, name='do_exam'),  # 更新这个路径
    path('student/do_exam/<int:exam_id>/', do_exam, name='do_exam'),
    path('student/exam_result/<int:score>/', exam_result, name='exam_result'),
    re_path(r'^student/exam_result/(?P<score>\d+(\.\d+)?)/$', exam_result, name='exam_result'),
    path('logout/', logout_view, name='logout'),
    path('student_register/', add_student, name='student_register'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('teacher/select_question_type/', select_question_type, name='select_question_type'),
    path('teacher/create_single_choice_question/', create_single_choice_question, name='create_single_choice_question'),
    path('teacher/create_multiple_choice_question/', create_multiple_choice_question, name='create_multiple_choice_question'),
    path('teacher/create_true_false_question/', create_true_false_question, name='create_true_false_question'),
    path('teacher/create_short_answer_question/', create_short_answer_question, name='create_short_answer_question'),

]

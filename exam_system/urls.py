from django.contrib import admin
from django.urls import path, include
from exam_app.views import home, do_exam
from exam_app.views_teacher import teacher_home
from exam_app.views_student import student_home, do_exam, logout_view,  exam_result
from exam_app.views_admin import add_student
from exam_app.views_admin import admin_home, add_teacher, add_student, edit_teacher, delete_teacher, edit_question, delete_question
from exam_app.views_admin import (
    admin_home, add_teacher, edit_teacher, delete_teacher,
    add_student, add_single_choice_question, add_multiple_choice_question,
    add_true_false_question, add_short_answer_question, edit_question, 
    delete_question, add_exam, edit_exam, delete_exam, choose_question_type
)

urlpatterns = [
    path('admin/add_teacher/', add_teacher, name='add_teacher'),
    path('admin/edit_teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('admin/delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('admin/add_student/', add_student, name='add_student'),
    path('admin/add_single_choice_question/', add_single_choice_question, name='add_single_choice_question'),
    path('admin/add_multiple_choice_question/', add_multiple_choice_question, name='add_multiple_choice_question'),
    path('admin/add_true_false_question/', add_true_false_question, name='add_true_false_question'),
    path('admin/add_short_answer_question/', add_short_answer_question, name='add_short_answer_question'),
    path('admin/edit_question/<int:question_id>/', edit_question, name='edit_question'),
    path('admin/delete_question/<int:question_id>/', delete_question, name='delete_question'),
    path('admin/add_exam/', add_exam, name='add_exam'),
    path('admin/edit_exam/<int:exam_id>/', edit_exam, name='edit_exam'),
    path('admin/delete_exam/<int:exam_id>/', delete_exam, name='delete_exam'),
    path('login/admin/', admin_home, name='admin_home'),
    path('admin/choose_question_type/', choose_question_type, name='choose_question_type'),  # Add this line
     
    path('api/', include('exam_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),  
    path('login/', include('exam_app.urls')),  
    path('teacher/', teacher_home, name='teacher_home'),
    # path('login/questions/', question_list, name='question_list'), 
    path('do_exam', do_exam, name='do_exam'), 
    path('student/', student_home, name='student_home'),
    path('student/do_exam/', do_exam, name='do_exam'),  
    path('logout/', logout_view, name='logout'),
    path('student/do_exam/<int:exam_id>/', do_exam, name='do_exam'),
    path('student/exam_result/<int:score>/', exam_result, name='exam_result'),
    path('student_register/', add_student, name='student_register'),
    
]

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('exam_app.urls')),  # 替换 'your_app_name' 为您的应用程序名称
# ]
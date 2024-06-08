from django.contrib import admin
from django.urls import path, include
from exam_app.views import home, questions, question_list, do_exam
from exam_app.views_teacher import teacher_home
from exam_app.views_student import student_home, do_exam, logout_view,  exam_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('exam_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),  
    path('login/', include('exam_app.urls')),  
    path('teacher/', teacher_home, name='teacher_home'),
    path('login/questions/', question_list, name='question_list'), 
    path('do_exam', do_exam, name='do_exam'), 
    path('student/', student_home, name='student_home'),
    path('student/do_exam/', do_exam, name='do_exam'),  
    path('logout/', logout_view, name='logout'),
    path('student/do_exam/<int:exam_id>/', do_exam, name='do_exam'),
    path('student/exam_result/<int:score>/', exam_result, name='exam_result'),

]

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('exam_app.urls')),  # 替换 'your_app_name' 为您的应用程序名称
# ]
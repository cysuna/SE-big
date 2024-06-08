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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, questions
from .views_auth import login, teacher_login, admin_login
from .views_teacher import teacher_home
from .views_admin import admin_home, add_teacher, edit_teacher, delete_teacher, add_question, edit_question, delete_question

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    path('teacher_login/', teacher_login, name='teacher_login'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_home/', admin_home, name='admin_home'),
    path('admin/add_teacher/', add_teacher, name='add_teacher'),
    path('admin/edit_teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('admin/delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('admin/add_question/', add_question, name='add_question'),
    path('admin/edit_question/<int:question_id>/', edit_question, name='edit_question'),
    path('admin/delete_question/<int:question_id>/', delete_question, name='delete_question'),
    path('questions/', questions, name='questions'),
]

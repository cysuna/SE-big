from django.contrib import admin
from django.urls import path, include
from exam_app.views import home
from exam_app.views_teacher import teacher_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('exam_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),  
    path('login/', include('exam_app.urls')),  
    path('teacher/', teacher_home, name='teacher_home'),
]

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('exam_app.urls')),  # 替换 'your_app_name' 为您的应用程序名称
# ]

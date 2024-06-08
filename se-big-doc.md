### 项目概述

这个项目是一个题库管理与在线考试系统，包含前端和后端两部分。前端使用 Vue.js、Axios 和 Element UI 实现，后端使用 Django 和 Django REST framework 实现。下面是前后端 API 的介绍。

### 目录

1. [前端 API 介绍](#前端-api-介绍)
2. [后端 API 介绍](#后端-api-介绍)

## 前端 API 介绍

### 1. 安装依赖

确保你已经安装了项目所需的依赖：

```bash
npm install
```

### 2. 项目结构

```plaintext
exam-system-frontend/
├── node_modules/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── assets/
│   ├── components/
│   │   └── HelloWorld.vue
│   ├── router/
│   │   └── index.js
│   ├── services/
│   │   └── api.js
│   ├── store/
│   │   └── index.js
│   ├── views/
│   │   ├── Home.vue
│   │   └── Questions.vue
│   ├── App.vue
│   ├── main.js
├── .eslintrc.js
├── .gitignore
├── babel.config.js
├── package.json
├── README.md
└── vue.config.js
```

### 3. 前端主要文件介绍

#### src/main.js

项目入口文件，初始化 Vue 实例并引入 Element UI：

```javascript
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
```

#### src/services/api.js

封装 Axios 请求：

```javascript
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getQuestions() {
    return apiClient.get('/questions/')
  },
  // 其他API调用方法
}
```

#### src/router/index.js

配置项目路由：

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Questions from '../views/Questions.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/questions',
    name: 'Questions',
    component: Questions
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```

#### src/views/Questions.vue

显示题目列表的组件：

```vue
<template>
  <div>
    <el-table :data="questions" style="width: 100%">
      <el-table-column prop="question_text" label="Question" width="400"></el-table-column>
      <el-table-column prop="question_type" label="Type" width="150"></el-table-column>
      <el-table-column prop="difficulty" label="Difficulty" width="100"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'Questions',
  data() {
    return {
      questions: []
    }
  },
  created() {
    this.fetchQuestions()
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await api.getQuestions()
        this.questions = response.data
      } catch (error) {
        console.error('Failed to fetch questions:', error)
      }
    }
  }
}
</script>
```

## 后端 API 介绍

### 1. 安装依赖

确保你已经安装了项目所需的依赖：

```bash
pip install -r requirements.txt
```

### 2. 项目结构

```plaintext
exam_system/
├── exam_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── views_home.py
│   ├── views_auth.py
│   ├── urls.py
├── exam_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   ├── home.html
│   ├── login.html
├── manage.py
├── requirements.txt
```

### 3. 后端主要文件介绍

#### exam_system/urls.py

配置项目路由：

```python
from django.contrib import admin
from django.urls import path, include
from exam_app.views_home import home
from exam_app.views_auth import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('exam_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),
    path('login/', login, name='login'),  # 添加这一行
]
```

#### exam_app/urls.py

应用级 URL 配置：

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### exam_app/models.py

定义模型：

```python
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
```

#### exam_app/serializers.py

定义序列化器：

```python
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
```

#### exam_app/views.py

定义视图集：

```python
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
```

#### exam_app/views_home.py

定义主页视图：

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

#### exam_app/views_auth.py

定义登录视图：

```python
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
```

#### exam_system/settings.py

确保设置正确：

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'exam_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'exam_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 确保这一行存在
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'exam_system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',


    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
]
```

### 4. 运行项目

#### 运行后端

1. 应用迁移并启动开发服务器：

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### 运行前端

2. 启动前端 Vue.js 开发服务器：

在前端项目根目录运行以下命令：

```bash
npm run serve
```

确保在浏览器中访问 `http://localhost:8080` 查看前端应用，并与后端 API 进行交互。


# SE-big
实验2&amp;大实验

•	后端：Python + Django/Flask + Django Rest Framework (DRF)
•	前端：vue.js + Axios (用于HTTP请求) + element- UI (用于前端组件)

```exam-system-frontend/
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
├── .gitignore
├── babel.config.js
├── package.json
├── README.md
└── vue.config.js
```
```your_project/
    your_app_name/
        templates/
            home.html
        __init__.py
        views.py
        urls.py
    your_project/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    manage.py```


## 快速入门
运行项目

启动后端 Django 服务器：
python3 manage.py runserver

启动前端 Vue.js 项目：
npm run serve

在浏览器中访问 http://localhost:8080/questions 查看题目列表。
这样配置后，你的前端 Vue.js 应用可以通过 Axios 调用后端 Django API，并使用 Element UI 展示数据。如果需要进一步定制功能，可以在 Vue 组件中继续扩展。

## 重建数据库

#### a. 删除现有的 SQLite 数据库文件

删除项目目录中的 `db.sqlite3` 文件：

```bash
rm db.sqlite3
```

#### b. 删除现有的迁移文件（如果需要）

在 `exam_app/migrations/` 目录中删除除 `__init__.py` 以外的所有文件：

```bash
rm exam_app/migrations/0*.py
```

#### c. 重新生成迁移文件

生成新的迁移文件：

```bash
python manage.py makemigrations exam_app
```

#### d. 重新应用迁移

应用迁移以创建新的数据库表：

```bash
python manage.py migrate
```

### 2. 检查模型和迁移文件的一致性

确保 `exam_app/models.py` 文件和迁移文件之间没有不一致的地方。例如，确保模型定义正确，并且所有字段都符合要求。

### 3. 确认模型定义

确保 `models.py` 文件中模型定义正确，如下所示：

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

### 4. 重新迁移和创建数据库表的详细步骤

1. 删除现有数据库文件：

```bash
rm db.sqlite3
```

2. 删除现有迁移文件：

```bash
rm exam_app/migrations/0*.py
```

3. 重新生成迁移文件：

```bash
python manage.py makemigrations exam_app
```

4. 重新应用迁移：

```bash
python manage.py migrate
```

5. 启动开发服务器：

```bash
python manage.py runserver
```

## 安装依赖

你的错误信息表明在启动Django服务器时，无法找到`corsheaders`模块。这通常是因为没有安装`django-cors-headers`库。你可以通过以下步骤解决这个问题：

### 1. 安装`django-cors-headers`

在你的终端中运行以下命令以安装`django-cors-headers`库：

```bash
pip install django-cors-headers
```

### 2. 确认安装成功

确保在你的虚拟环境或Python环境中成功安装了该库，可以使用以下命令查看已安装的包：

```bash
pip list
```

检查输出中是否包含`django-cors-headers`。

### 3. 更新`INSTALLED_APPS`

确保在你的`settings.py`文件中正确添加了`corsheaders`到`INSTALLED_APPS`：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',  # 确保这一行存在
    'exam_app',
]
```

### 4. 配置`MIDDLEWARE`

确保在你的`settings.py`文件中正确配置了中间件：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 确保这一行存在
]
```

### 5. 重新启动服务器

完成以上步骤后，重新启动Django开发服务器：

```bash
python manage.py runserver
```

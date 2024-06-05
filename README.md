# SE-big
实验2&amp;大实验

## 快速入门
 运行项目
确保你已经安装了所需的库：

pip install django djangorestframework django-cors-headers
创建并应用数据库迁移：


python manage.py makemigrations
python manage.py migrate
创建超级用户以访问Django admin界面：


python manage.py createsuperuser
运行开发服务器：


python manage.py runserver
这样，你的Django项目就完成了基础配置，并可以与React前端进行通信。你可以通过http://localhost:8000/admin访问Django admin界面，通过http://localhost:8000/api/questions/访问API端点。

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

# SE-big
实验2&amp;大实验


## 快速入门
运行项目

启动后端 Django 服务器：
```
python3 manage.py runserver
```
启动前端 Vue.js 项目：
```
npm run serve
```

在浏览器中访问 http://localhost:8000进入主页

## 重建数据库
```bash
rm db.sqlite3
rm exam_app/migrations/0*.py
python3 manage.py makemigrations exam_app
python3 manage.py migrate
python3 manage.py createsuperuser
```

## 安装依赖

安装`django-cors-headers`

```bash
pip install django-cors-headers
```




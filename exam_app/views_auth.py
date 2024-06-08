from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('student_home')  # 重定向到做题界面
        else:
            messages.error(request, '用户名或密码错误')
            return render(request, 'login.html')
    return render(request, 'login.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.groups.filter(name='Teachers').exists():
            auth_login(request, user)
            return redirect('teacher_home')
        else:
            messages.error(request, '用户名或密码错误，或您没有教师权限')
            return render(request, 'teacher_login.html')
    return render(request, 'teacher_login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('admin_home')
        else:
            messages.error(request, '用户名或密码错误，或您没有管理员权限')
            return render(request, 'admin_login.html')
    return render(request, 'admin_login.html')
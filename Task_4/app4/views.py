from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def main(request):
    response = """
    <h2>Регистрация</h2>
    <form method='POST' action='/register/'>
        <label for='username'>Логин:</label>
        <input type='text' id='username' name='username'><br>
        <label for='password'>Пароль:</label>
        <input type='password' id='password' name='password'><br>
        <button type='submit'>Зарегистрироваться</button>
    </form>

    <h2>Авторизация</h2>
    <form method='POST' action='/login/'>
        <label for='login_username'>Логин:</label>
        <input type='text' id='login_username' name='username'><br>
        <label for='login_password'>Пароль:</label>
        <input type='password' id='login_password' name='password'><br>
        <button type='submit'>Войти</button>
    </form>
    """
    return HttpResponse(response)
@csrf_exempt
def register(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponse("<p>Заполните все поля, пожалуйста! :З</p>")
        if User.objects.filter(username=username).exists():
            return HttpResponse("<p>Пользователь с таким никнэймом уже существует.</p>")
        User.objects.create_user(username=username, password=password)
        return HttpResponse("<p>Вы стали одним из Хокаге!</p>")

    return HttpResponse("<p>Ерундой занимаетесь...</p>")


@csrf_exempt
def login_(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponse("<p>Заполните все поля, пожалуйста! :З</p>")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponse("<p>Добро пожаловать, Хозяин!</p>")
        else:
            return HttpResponse("<p>У нас таких нет.</p>")

    return HttpResponse("<p>Ерундой занимаетесь...</p>")

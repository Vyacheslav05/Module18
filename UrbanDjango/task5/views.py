from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .apps import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            # Дополнительная логика
    else:
        form = UserRegisterForm()

    return render(request, 'fifth_task/registration_page.html', {'form': form})

from django.shortcuts import render
from .apps import UserRegisterForm

# Псевдо-список существующих пользователей
users = ['user1', 'user2', 'user3']

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            if password != form.cleaned_data['repeat_password']:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/success.html', {'username': username})
    else:
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

from django.shortcuts import render

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/success.html', {'username': username})

    return render(request, 'fifth_task/registration_page.html', info)
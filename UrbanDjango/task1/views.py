
### - 29.12.24 (+)

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django import forms
from task1.models import Buyer, Game                          # - (+) Импортируем модели

context = {
        'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    }
def menu_task(request):
    return render(request, "fourth_task/menu.html")

def platform_task(request):
    return render(request, "fourth_task/platform.html")

def games_task(request):
    return render(request, "fourth_task/games.html", context)

def cart_task(request):
    return render(request, "fourth_task/cart.html")

###____________________________________________________________________________________________________
# Псевдо-список существующих пользователей
existing_users = ['user1', 'user2', 'user3']

# Форма для регистрации
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите свой возраст')


def sign_up_by_django(request):
    info = {}
    error = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            # Проверка существования пользователя в таблице Buyer
            if Buyer.objects.filter(name=username).exists():
                error = "Пользователь уже существует."
                form.add_error('username', error)
            elif age < 18:
                error = "Вы должны быть старше 18."
                form.add_error('age', error)
            elif password != repeat_password:
                error = "Пароли не совпадают."
                form.add_error('repeat_password', error)
            else:
                # Создание нового покупателя
                Buyer.objects.create(name=username, balance=0, age=age)  # Добавляем покупателя в БД
                return HttpResponse(f"Приветствуем, {username}!")

    else:
        form = SignUpForm()

    info['error'] = error
    return render(request, 'registration_page.html', {'info': info, 'form': form})

def games_task(request):
    games = Game.objects.all()  # Получаем все записи из таблицы Game
    return render(request, "fourth_task/games.html", {'games': games})  # Передаем коллекцию игр в контекст


# def sign_up_by_django(request):
#     info = {}                                                                     # Пустой словарь для контекста
#     error = None                                                                  # Переменная для хранения ошибок
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             # Обработка данных из POST запроса
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = int(form.cleaned_data['age'])                                   # Преобразуем возраст в целое число
#
#             # Проверка существования пользователя
#             if username in existing_users:
#                 error = "Пользователь уже существует."
#                 form.add_error('username', error)                            # Добавляем ошибку к полю логина
#             # Проверка возраста
#             elif age < 18:
#                 error = "Вы должны быть старше 18."
#                 form.add_error('age', error)                                 # Добавляем ошибку к полю возраста
#             # Проверка совпадения паролей
#             elif password != repeat_password:
#                 error = "Пароли не совпадают."                            # Добавляем ошибку к полю повторного пароля
#                 form.add_error('repeat_password', error)
#             else:
#                 # Здесь можно добавить логику для сохранения пользователя
#                 existing_users.append(username)  # Добавляем пользователя в список
#                 return HttpResponse(f"Приветствуем, {username}!")
#
#     else:
#         form = SignUpForm()
#
#     info['error'] = error                                                         # Добавление ошибки в словарь info
#     return render(request, 'registration_page.html', {'info': info, 'form': form, 'existing_users': existing_users})




def sign_up_by_html(request):
    info = {}                                                                     # Пустой словарь для контекста
    error = None                                                                  # Переменная для хранения ошибок
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка существования пользователя
        if username in existing_users:
            error = "Пользователь уже существует."

        # Проверка возраста
        elif int(age) < 18:
            error = "Вы должны быть старше 18."

        # Проверка совпадения паролей
        elif password != repeat_password:
            error = "Пароли не совпадают."                                         # Добавляем ошибку в словарь

        else:
            # Здесь можно добавить логику для проверки и сохранения пользователя
            existing_users.append(username)                                        # Добавляем пользователя в список
            return HttpResponse(f"Приветствуем, {username}!")

    info['error'] = error  # Добавление ошибки в словарь info
    return render(request, 'registration_page.html', {'info': info, 'existing_users': existing_users})

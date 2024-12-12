from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


def one(request):
    text = 'Главная страница'
    context = {
        'text1': text
    }
    return render(request, "platform.html", context)


def two(request):
    text = 'Игры'
    games = Game.objects.all()
    context = {
        'text2': text,
        'games': games
    }
    return render(request, "games.html", context)


def three(request):
    text = 'Корзина'
    dop = 'Извините, ваша корзина пуста'
    context = {
        'text': text,
        'text3': dop
    }
    return render(request, "cart.html", context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=name).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=name, password=password, age=age, balance=balance)
                return render(request, 'registration_page.html', {'form': form, 'info': f"Приветствуем, {name}!"})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info.get('error')})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(username=username, password=password, age=age, balance=balance)
                return render(request, 'registration_page.html', {'form': form, 'info': f"Приветствуем, {username}!"})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info.get('error')})
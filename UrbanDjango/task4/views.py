from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

def home_view(request):
    return render(request, 'fourth_task/platform.html')

# def games_view(request):
#     items = ['Игра 1', 'Игра 2', 'Игра 3']
#     return render(request, 'fourth_task/games.html', {'items': items})

def games_view(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')

def buy_game_view(request, game_name):
    return redirect('cart')
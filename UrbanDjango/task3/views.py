from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    items = ['Игра 1', 'Игра 2', 'Игра 3']
    return render(request, 'third_task/games.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')
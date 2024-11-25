"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.views.generic import TemplateView
# from UrbanDjango.task2.views import func_templ, class_templ
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('func/', func_templ),
#     path('class/', class_templ.as_view()),
# ]

from django.contrib import admin
from django.urls import path, include
# from task2.views import func_templ, class_templ
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('func_templ/', func_templ, name='func_templ'),
#     path('class_templ/', class_templ.as_view(), name='class_templ'),
# ]

from django.contrib import admin
from django.urls import path, include
# from task4.views import home_view, games_view, cart_view, buy_game_view

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home_view, name='home'),
#     path('games/', games_view, name='games'),
#     path('cart/', cart_view, name='cart'),
#     path('buy/<str:game_name>/', buy_game_view, name='buy_game'),
# ]
from django.urls import path
from task5.views import register, sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', sign_up_by_django, name='sign_up_by_django'),
    path('register/', register, name='register'),
    path('django_sign_up/', sign_up_by_html, name='sign_up_by_html'),
]
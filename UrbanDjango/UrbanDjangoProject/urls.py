"""
URL configuration for UrbanDjangoProject project.

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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# from UrbanDjangoProject.task2.views import func_templ, class_templ
from UrbanDjango.task2.views import func_templ, class_templ

urlpatterns = [
    path('func/', func_templ),
    path('class/', class_templ.as_view()),
]

# from django.contrib import admin
# from django.urls import path
# from UrbanDjango.task2.views import func_templ, class_templ
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('func_templ/', func_templ, name='func_templ'),
#     path('class_templ/', class_templ.as_view(), name='class_templ'),
# ]

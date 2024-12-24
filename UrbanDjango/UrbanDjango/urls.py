"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include                             ### - (+)

### - 15.12.24
### - 15.12.24 (+)
### - 20.12.24 (++)
### - 22.12.24 (+++)

# from task2.views import func_temp, class_temp
#from task3.views import platform_task, games_task, cart_task   ### - 18.12.24 task3 переехал в task4
from task5.views import sign_up_by_django, sign_up_by_html
from django.views.generic import TemplateView

urlpatterns = [
    path('', sign_up_by_django),                                   ### - (++)
    path('django_sign_up/', sign_up_by_html),                      ### - (++)
    path('admin/', admin.site.urls),                               ### - (+)
]

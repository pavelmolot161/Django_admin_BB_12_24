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
### - 15.12.24
### - 15.12.24 (+)
### - 20.12.24 (++)
### - 22.12.24 (+++)
### - 22.12.24 (++++)
from django.contrib import admin
from django.urls import path, include                              ### - (+)
# from task2.views import func_temp, class_temp
#from task3.views import platform_task, games_task, cart_task      ### - 18.12.24 task3 переехал в task4
from task1.views import sign_up_by_django, sign_up_by_html                  ### - (++++)
from django.views.generic import TemplateView
from task1.views import platform_task, games_task, cart_task, menu_task     ### - (++++)                                      ### - (++++)
from task1 import views

app_name = 'task1'                                                 ### - (++++)

urlpatterns = [
    path('', views.sign_up_by_django, name='sign_up'),
    path('django_sign_up/', views.sign_up_by_html, name='sign_up_html'),
    path('admin/', admin.site.urls),
    path('platform', platform_task, name='platform_task'),
    path('menu', menu_task, name='menu_task'),
    path('games', games_task, name='games_task'),
    path('cart', cart_task, name='cart_task'),
]




# urlpatterns = [
#     path('', sign_up_by_django),                                   ### - (++)
#     path('django_sign_up/', sign_up_by_html),                      ### - (++)
#     path('admin/', admin.site.urls),                               ### - (+)
#     path('menu_task/', menu_task, name="menu"),                               ### - (++++)
#     path('platform_task/', platform_task, name="platform"),                       ### - (++++)
#     path('games_task/',games_task, name="games"),                              ### - (++++)
#     path('cart_task/',cart_task, name="cart"),                                ### - (++++)
# ]



###______________________________________________________________________________________________________

# from django.contrib import admin
# from django.urls import path
#
# ### - 18.12.24 (+)
# from task4 import views
#
# urlpatterns = [
#
#     path('menu_task/', views.menu_task),                               ### - (+)
#     path('platform_task/', views.platform_task),                       ### - (+)
#     path('games_task/',views.games_task),                              ### - (+)
#     path('cart_task/',views.cart_task),                                ### - (+)
# ]

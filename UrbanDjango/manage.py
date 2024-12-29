#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#####################################################################################################

### - 15.12.24 - переход в корневую папку UrbanDjango
### - 14.12.24
### - Эта команда вернет на один уровень выше в адресной строке:
#                                                            >>> cd ..

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                               >>> django.get_version()

### - 4) Создание проекта: - (.venv) PS D:\module_18_Django> >>> django-admin startproject mysite

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                            (.venv) PS D:\module_18_Django> >>> cd mysite
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py startapp app

### - 8) Создание файла зависимостей:
#             (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt
#     8.a) вывод зависимостей в консоль:
#                                                            >>> pip freeze

'''Выполнен 1 пункт выполнен, 2 пункт выполнен, 3 пункт - не сработал, 4 пункт выполнен,
            7 пункт выполнен - создано 3 приложения с названиями 'example1', 'example2', 'example3'
            8 пункт выполнен - создан файл зависимостей requirements.txt.
            8 пункт выполнен сработал.
           '''

### - 15.12.24
### - 9) Создали приложение - task2
### - 10) Создали папку templates и в ней папку second_task:
##        - создаем 2 HTML шаблона - class_template.html, func_template.html

### - 11) В приложении task2 в файле views.py добавили:
##                   def func_temp(request):
#                       return render(request, "func_template.html")
#
#                    class class_temp(TemplateView):
#                       template_name = "class_template.html"

### - 15.12.24     ____________________________________________________________________________________________
### - Поменял структуру проэкта и определил корневую папку UrbahDjango.
                        # 1- Откройте PyCharm.
                        # 2 - Перейдите в меню File -> Open....
                        # 3 - Выберите папку, которую хотите установить в качестве корня проекта.
                        # 4 - PyCharm автоматически установит выбранную папку как корень проекта.

### - 12) Внесение дополнений в папку UrbahDjango файл urls.py:
                        # urlpatterns = [
                        #     path('admin/', admin.site.urls),
                        #     path('', func_temp),
                        #     path('class_temp_sample/', class_temp.as_view())]

### - 13) ЗАПУСK НОВЫЙ серверa разработки, (выполнив команду из корневого каталога проекта):
#                     PS D:\module_18_Django_DZ\UrbanDjango> >>> python manage.py runserver

### - 14) Созданы 2 новых файла HTML в папке templates c названием class_template.html, func_template.html.

### - 16.12.24   ____________________________________________________________________________________________

### - 15) Cоздали папку third_task в директории templates.
### - 16) Cоздали новое приложение task3  для представлений.
### - 17) Созданы 3 новых файла HTML в папке templates/third_task c названием cart.html, games.html, platform.html

### - 18.12.24

### - 18) Cоздали папку fourth_task в директории templates скопировали в нее файлы cart.html, games.html, platform.html
# и создали новый файл menu.html.

### - 19) Создали новое приложение task4 и перенесем в него все данные из task3.

### - 20) Внесены дополнения в views папки task4:
#               def platform_task(request):
#                   context =  {                                                                 ### - (+)
#                       'games': ["Atomic Heart", "Cyberpunk 2077"]
#               }
#               return render(request, "fourth_task/platform.html", context)

### - ) Внесены дополнения в файл views.py папки app которая связана с файлами html:
# def index(request):
#     title = "Заголовок мой сайт (1.a)"
#     text = 'мой текст (10)'
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return render(request, "index.html", context)

### - 20) Внесены изменения в urls.py папки UrbanDjango:
#               urlpatterns = [
#                   path('menu', menu_task)                                 ### - (+)

###______________________________________________________________________________________
###
''' - Склонирован проэкт, после этого привязан к новому репозиторию и стал отдельным проектом '''

### - 21) Первым делом необходимо установить библиотеки и зависимости:
#         - Переходим в дерикторию где расположен файл requirements.txt (UrbanDjango)
#                        (.venv) PS D:\Rabota_12_24\Django_admin_BB_12_24> >>> cd UrbanDjango
#         - Устанавливаем зависимости:
#            (.venv) PS D:\Rabota_12_24\Django_admin_BB_12_24\UrbanDjango> >>> pip install -r requirements.txt
### - 22) Устанавливаем приложение task5:
#            (.venv) PS D:\Rabota_12_24\Django_admin_BB_12_24\UrbanDjango> >>> python manage.py startapp task5

### - (23) Сменили корневую папку:
### - Поменял структуру проэкта и определил корневую папку UrbahDjango.
                        # 1- Откройте PyCharm.
                        # 2 - Перейдите в меню File -> Open....
                        # 3 - Выберите папку, которую хотите установить в качестве корня проекта.
                        # 4 - PyCharm автоматически установит выбранную папку как корень проекта.

### - _____________________________________________________________________________________________

                                        ### - 19 модуль Django DZ 1
### - 24) Создали модели в task1/models:
#              Созданы две модели: Buyer и Game.
#              В модели Buyer добавлены поля name, balance и age.
#              В модели Game добавлены поля title, cost, size, description, age_limited и связь с моделью Buyer
#              через ManyToManyField.

### - 25)  создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:

#                     D:\Rabota_12_24\Django_admin_BB_12_24\UrbanDjango> >>> python manage.py makemigrations
#                     D:\Rabota_12_24\Django_admin_BB_12_24\UrbanDjango> >>> python manage.py migrate

### - 26)

###________________________________________________________________________________________________________

                                        ### - 19 модуль Django DZ 2

### - 27) Проверили текущие ветки с помощью команды:
#                                                    >>> git branch    ### - >>> * main

### - 28) Создали новую ветку для второго домашнего задания:
#                                                    >>> git checkout -b M_19_homework_2

### - 29) Эта команда запускает интерактивную оболочку Python с доступом к Вашему проекту Django:
#                                                      >>> python manage.py shell

### - 30) Импортируем модель для запросов из приложения task1:
#                                                      >>> from task1.models import Buyer

### - 31) Запрос на заполнение таблици. в таблице, связанной с моделью Buyer, будет создана новая запись
# с указанными значениями для полей name и balance, age:
#                                              >>> Buyer.objects.create(name="Pavel", balance=7, age=16)
#                                              >>> Buyer.objects.create(name="Viktor", balance=3, age=22)
#                                              >>> Buyer.objects.create(name="Andrey", balance=5, age=33)

### - 32) Импортируем модель для запросов из приложения task1:
#                                                      >>> from task1.models import Game

### - 33) Запрос на заполнение таблици. в таблице, связанной с моделью Game, будет создана новая запись
# с указанными значениями для полей title и cost, size, description, age_limited, buyers:
#     >>> Game.objects.create(title="The Witcher 3", cost=9, size=3, description="Epic fantasy RPG adventure", age_limited=True)
#     >>> Game.objects.create(title="Counter-Strike", cost=6, size=4, description="Competitive team-based shooter", age_limited=False)
#     >>> Game.objects.create(title="Minecraft ", cost=7, size=6, description="Creative block-building sandbox", age_limited=False)

### - 34) Связываем поле buyer с записями Game (Присваиваем значения через id)
#     >>> Game.objects.get(id=1).buyers.set([Andrey])
#     >>> Game.objects.get(id=2).buyers.set([Andrey])
#     >>> Game.objects.get(id=3).buyers.set([Andrey])

#___________________________________________________________________________________________________________

                                      ### - 19 модуль Django DZ 3

### - Слияние 4 и 5 ДЗ в одно

### - 35) ЗАПУСK НОВЫЙ серверa разработки, (выполнив команду из корневого каталога проекта):
#                     PS D:\module_18_Django_DZ\UrbanDjango> >>> python manage.py runserver
#___________________________________________________________________________________________________________































###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

### - Отдельный блок работы с ВЕТКАМИ

# Проверьте текущие ветки с помощью команды:
#                                                    >>> git branch

# Создайте новую ветку для второго домашнего задания:
#                                                    >>> git checkout -b M_19_homework_2

# Добавьте и зафиксируйте изменения (ВНИМАНИЕ точка через пробел после add):
#                                                    >>> git add .
#                                                    >>> git commit -m "Добавлено второе домашнее задание"
# Отправьте ветку на удалённый репозиторий:
#                                                    >>> git push origin homework_2

# Переключитесь на ветку, от которой хотите создать новую ветку:
#                                                    >>> git checkout homework_2
# Создайте новую ветку от текущей. Например, если Вы хотите создать ветку для доработки второго задания:
#                                                    >>> git checkout -b homework_2_update
# Внесите изменения в код и зафиксируйте их:
#                                                    >>> git add .
#                                                    >>> git commit -m "Доработка второго домашнего задания"
# Отправьте новую ветку на удалённый репозиторий:
#                                                    >>> git push origin homework_2_update

# Чтобы вернуться на родительскую ветку (или на ветку выше) в Git, Вы можете использовать команду git checkout.
# Вот как это сделать:
# Посмотрите список веток и определите, на какую ветку хотите вернуться:
#                                                >>> git branch

# Переключитесь на нужную ветку. Например, если Вы хотите вернуться на ветку homework_2, выполните:
#                                                >>> git checkout homework_2

# Если Вы хотите вернуться на последнюю ветку, на которой Вы были, эта команда переключит вас на последнюю
# использованную ветку:
#                                                >>> git checkout -

# Если у Вас есть незавершенные изменения в текущей ветке, Git не позволит Вам переключиться на другую ветку,
# пока Вы не зафиксируете или не отмените эти изменения. Вы можете либо зафиксировать изменения, либо
# использовать git stash, чтобы временно сохранить их:
#                                                >>> git stash

# После этого Вы сможете переключиться на другую ветку. Когда будете готовы, Вы можете восстановить
# сохраненные изменения с помощью:
#                                                >>> git stash pop


###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

### - Отбельный блок QuerySet ЗАПРОСЫ ()

### - 1) Эта команда запускает интерактивную оболочку Python с доступом к Вашему проекту Django:
#                                                      >>> python manage.py shell
### - 2) Импортируем модель для запросов из приложения app:
#                                                      >>> from app.models import Author
### - 3) Извлекает все записи из таблицы, связанной с моделью Author. Он возвращает QuerySet, содержащий всех авторов:
#                                                      >>> Author.objects.all()
### - 4) Запрос на заполнение таблици. в таблице, связанной с моделью Author, будет создана новая запись
# с указанными значениями для полей name и bio:
#                                                      >>> Author.objects.create(name="New Author", bio="test")
### - 5) Узнаем сколько пустых данных в таблице:
#                                                      >>> Author.objects.filter(bio="")

### - 6) Замена данных в таблице, возвращает количество замененных элементов:
#                                                      >>> Author.objects.filter(bio="test2").update(bio="Zamena1")

### - 7) Найти количество объектов в БД, возвращает количество элементов:
#                                                      >>> Author.objects.count()

### - 8) Ищет автора с id=2 в базе данных и сохраняет его в переменной a. Если автора нет, возникает ошибка:
#                                                      >>> a = Author.objects.get(id=2)
#                                                      >>> a                        ### - >>> <Author: Two Author2>
### - 9) УДАЛЕНИЕ объектов в БД:
#                                                      >>> a.delete()

### - 8) Все объекты из базы данных сохраняем в переменной a:
#                                              >>> a = Author.objects.all()
#                                              >>> a   ### - >>> <QuerySet [<Author: New Author>, <Author: Author3>]>
### - 9) ВЫХОД из консоли:
#                                              >>> exit()

###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#################  ИЗ ЛЕКЦИИ #################################################################################

##############################################################################################################
### index2.html 18.12.24
#
# {% extends 'index.html' %}          <!-- extends Указывает от какого шаблона будет наследоватся, или кто родительский класс-->
#
# {% block title %}Home - {{ block.super }}{% endblock %}
# <!---->
# {% block header %}
#     {{ block.super }}                                            <!--Прийдет инфа из другого блока по наследованию-->
#     <h2>Welcome to the 2 Page</h2>
# {% endblock %}
#
# {% block content %}
#     <h2> Latest Posts </h2>
#     <ul>
#         <li>Post 1</li>               <!--Коментарий проверка-->
#         <li>Post 2</li>
#         <li>Post 3</li>
#     </ul>
# {% endblock %}                        <!--Закрытие блока проверка-->
#
# {% block footer %}
#     <p>Thanks for visiting</p>
#     {{ block.super }}                                      <!--Переносит инфу из блока footer родительского класса-->
# {% endblock %}
#
#

###################################################################################################################

### - index.html 18.12.24

# <!DOCTYPE html>
#
# <html lang="en">
# {% load static %}                                        <!--Импорт static или загрузка функции проверка-->
# <head>
#     <meta charset="UTF-8">
#     <title>{% block title %}My Site{% endblock %}</title>
#     <link rel = 'stylesheet' type="text/css" href="{% static 'style.css' %}">
# </head>
#
# <head>
# <body>
#     <header>
#         {% block header %}
#         <h1>Welcome to My Site 1</h1>
#         {% endblock %}
#     </header>
#
#     <nav>
#         {% block navigation %}
#         <ul>
#             <li><a href='/'>Home</a></li>
#             <li><a href='/about/'>About</a></li>
#             <li><a href='/contact/'>Contact</a></li>
#         </ul>
#         {% endblock %}
#     </nav>
#
#     <main>
#         {% block content %}
#             <p>Тут будут посты</p>                                          <!--Коментарий-->
#         {% endblock %}
#     </main>
#
    # <footer>
    #     {% block footer %}
    #         <p>2023 My Site</p>
    #     {% endblock %}
    # </footer>
# </body>
# </html>

##############################################################################################################

# {% extends 'menu.html' %}    <!-- extends Указывает от какого шаблона будет наследоватся, или кто родительский класс-->
#
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Platform(21)</title>
#     <style>
#                                     /* Добавляем стиль для ссылок */
#         a {
#             display: block;         /* Изменяем отображение на блочный элемент */
#             margin: 5px 0;          /* Добавляем отступы между ссылками */
#         }
#                                     /* Новый стиль для кнопки */
#         .button_1-container {
#             position: fixed;        /* Фиксированное позиционирование */
#             bottom: 10px;           /* Отступ от нижней границы */
#             left: 10px;             /* Отступ от левой границы */
#         }
#
#         .button_2-container {
#             position: fixed;        /* Фиксированное позиционирование */
#             bottom: 10px;           /* Отступ от нижней границы */
#             left: 160px;             /* Отступ от левой границы */
#         }
#
#         .small-button {
#             padding: 1px 3px;      /* Уменьшаем размеры кнопки */
#             font-size: 10px;        /* Уменьшаем размер шрифта */
#         }
#
#     </style>
# </head>
# <body>
#     <header>
#         {% block pagename %}                   <!--Заголовок страницы-->
#             {{ block.super }}                  <!--Переносит инфу из блока pagename родительского класса-->
#         {% endblock %}
#     </header>
#
#     <nav>
#         {% block menu %}
#             {{ block.super }}                  <!--Переносит инфу из блока menu родительского класса-->
#         {% endblock %}
#     </nav>
#
#     {% block content %}
#         {{ block.super }}                     <!--Переносит инфу из блока content родительского класса-->
#     {% endblock %}
#
#     <footer>                                  <!--Информация о сайте-->
#         {% block footer %}
#             {{ block.super }}                 <!--Переносит инфу из блока footer родительского класса-->
#         {% endblock %}
#     </footer>
#
#
#     <!--########################################################################################################-->
#
#     <div class="button_1-container">             <!--Кнопка внизу для навигации, не по заданию-->
#         <a href="http://127.0.0.1:8000/games">
#             <button class="small-button"><h4>На страничку c играми (16)</h4></button>
#         </a>
#     </div>
#
#      <div class="button_2-container">            <!--Кнопка внизу для навигации, не по заданию-->
#         <a href="http://127.0.0.1:8000/cart">
#             <button class="small-button"><h4>На страничку c корзиной (17)</h4></button>
#         </a>
#     </div>
# </body>
# </html>

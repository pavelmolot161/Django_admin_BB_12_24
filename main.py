
### - 13.12.24

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                                    >>> django.get_version()   ??? - не сработало

### - 4) Создание проекта: -      (.venv) PS D:\module_18_Django> >>> django-admin startproject UrbanDjango

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                                 (.venv) PS D:\module_18_Django> >>> cd UrbanDjango
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки, (выполнив команду из корневого каталога проекта):
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py startapp example1

### - 8) Создание файла зависимостей:
#                  (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt

'''Выполнен 1 пункт выполнен, 2 пункт выполнен, 3 пункт - не сработал, 4 пункт выполнен,
            7 пункт выполнен - создано 3 приложения с названиями 'example1', 'example2', 'example3'
            8 пункт выполнен - создан файл зависимостей requirements.txt.
            8 пункт выполнен сработал.
           '''


#




























##############################################################################################################

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

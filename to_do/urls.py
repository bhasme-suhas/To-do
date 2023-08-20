from django.contrib import admin
from django.urls import path,include
from .views import index,add_view,delete_view,mark_view

urlpatterns = [
    path('index/', index, name='todo_index'),
    path('add-todo/', add_view, name='add_todo'),
    path('delete-todo/<int:todo_id>', delete_view, name='delete_todo'),
    path('mark-todo/<int:todo_id>', mark_view, name='mark_todo'),
    # path('update_todo/<int:todo_id>', update_view, name='update_todo')

]
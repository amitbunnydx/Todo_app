
from django.urls import path
from . import views 

urlpatterns = [
    path('list/',views.todo_list),
    path("addtodo_list/",views.addtodo_list,name="insert"),
    path("delete_list/<int:todo_id>/",views.delete_list,name="delete"),
]
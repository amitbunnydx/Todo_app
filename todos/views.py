from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo

def todo_list(request):
    context={"todo_list": Todo.objects.all()}
    return render(request,"todo/todo_list.html",context)

def addtodo_list(request:HttpRequest):    
    todo=Todo(content = request.POST['content'])
    todo.save()
    return redirect("/todos/list/")

def delete_list(request,todo_id):
    todo_delete=Todo.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect("/todos/list/")

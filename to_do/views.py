from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
from django.http import HttpResponse

# Create your views here.
CONVERT_TO_BOOL = {"0":False,"1":True}

ORDER_TO_BOOL = {"0":"created_time","1":"-created_time"}

def index(request):
    search = request.GET.get("todosearch")
    completed = request.GET.get("completed")
    order = request.GET.get("order")
    all_todos = Todo.objects.all()
    #Search 
    if search != None:
        all_todos = all_todos.filter(title__icontains=search)
    if completed != None:
        value = CONVERT_TO_BOOL.get(completed)
        all_todos = all_todos.filter(completed = value)
    if order != None:
        value = ORDER_TO_BOOL.get(order)
        all_todos = all_todos.order_by(value) 
    data = {
        "todos" : all_todos
    }
    page_name = "index.html"
    return render(request, page_name, context= data)

def add_view(request):
    if request.method == "GET":
        return HttpResponse("Invalid Method")
    else:
        todo_input = request.POST['todoInput']
        Todo.objects.create(title = todo_input)
        return redirect('todo_index')
    
def delete_view(request, todo_id):
    if request.method == "POST":
        return HttpResponse("Invalid Method")
    else:
        try:
            todo_obj = Todo.objects.get(id = todo_id)
            todo_obj.delete()
            return redirect("todo_index")
        except Todo.DoesNotExist:
            return HttpResponse("Todo Not found")

def mark_view(request, todo_id):
    if request.method == "POST":
        return HttpResponse("Invalid Method")
    else:
        try:
            todo_obj = Todo.objects.get(id = todo_id)
            todo_obj.completed = True
            todo_obj.save()
            return redirect("todo_index")
        except Todo.DoesNotExist:
            return HttpResponse("Todo Not found")


# def update_view(request, todo_id):
#     if request.method == "POST":
#         return HttpResponse("Invalid Method")
#     else:
#         try:
#             todo_obj = Todo.objects.get(id = todo_id)
            
#             return redirect("todo_index")
#         except Todo.DoesNotExist:
#             return HttpResponse("Todo Not found")
        
        
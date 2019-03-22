
from django.shortcuts import render, redirect
from .models import Category, TodoList
# Create your views here.


def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    content = {"todos": todos, "categories": categories}

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/todolist")
        if "taskDelete" in request.POST:
            checkedlist = request.POST['checkedbox']
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, 'todolist/index.html', content)

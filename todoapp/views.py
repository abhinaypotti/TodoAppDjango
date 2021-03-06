from django.shortcuts import render, redirect
from .models import TodoModel
# Create your views here.
def index(request):
    mytodo = TodoModel.objects.all()
    context = {'mytodo':mytodo}
    return render(request,'index.html',context)


def addtask(request):
    mytask = request.POST['task']
    TodoModel(task=mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletetask(request,taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])

def edittaskview(request,taskpk):
    context = {'todopk':taskpk}
    return render(request,'edit.html',context)

def edittask(request,taskpk):
    userenterredtask = request.POST['task']
    todo = TodoModel.objects.filter(id = taskpk)[0]
    todo.task = userenterredtask
    todo.save()
    return render('indexpage')



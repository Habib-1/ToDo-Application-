from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.
def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    done_tasks=Task.objects.filter(is_completed=True)
    return render(request,'index.html',{'data':tasks, 'done_task':done_tasks})

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else :
        context={
            'get_task':get_task,
        }
    return render(request,'edit_page.html',context)

def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')

def delete_all(request):
    Task.objects.filter(is_completed=True).delete()

    return redirect('home')
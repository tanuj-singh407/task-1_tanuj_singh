from django.shortcuts import render

def task_page(request):
    return render(request, 'myapp/task.html')

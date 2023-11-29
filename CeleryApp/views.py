from django.shortcuts import render
from MyCelery_Project.celery import add
from .tasks import *
from celery.result import AsyncResult


# Create your views here.

# enqueue task using delay()
# def index(request):
#     print("Results: ")
#     result1 = add.delay(10, 20)
#     print(f'Result1:{result1}')
#     result2 = sub.delay(80, 10)
#     print(f'Result2:{result2}')
#     return render(request, "CeleryApp/home.html")

# enqueue task using apply_async() function
# def index(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[10,20])
#     print(f'Result1:{result1}')
#     result2 = sub.apply_async(args=[80, 10])
#     print(f'Result2:{result2}')
#     return render(request, "CeleryApp/home.html")


# Display addition value after task execution
def index(request):
    result = add.delay(10, 30)
    return render(request, "CeleryApp/home.html",{"result":result})

def about(request):
    return render(request, "CeleryApp/about.html")

def contact(request):
    return render(request, "CeleryApp/contact.html")

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    print(f"Ready:{result.ready()}")
    print(f"successfull:{result.successful()}")
    print(f"Failed:{result.failed()}")
    return render(request, 'CeleryApp/result.html',{"result":result})
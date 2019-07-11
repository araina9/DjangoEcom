from django.shortcuts import render
from django.http import HttpResponse
from .models import  Student

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Test Student Index Page</h1>")
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students':students})


# def student_show(request):
#     student = Student.objects.order_by("roll_no")
#     return render(request, 'student/')


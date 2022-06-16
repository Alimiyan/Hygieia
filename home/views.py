from django.shortcuts import render
from django.http import HttpResponse
from .models import Department

# Create your views here.
def index(request):
    fruits = {
        'fr': ['apple', 'banana', 'cherry'],
    }
    return render(request, 'index.html', fruits)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dic_dep = {
        'dept' : Department.objects.all(),
    }
    return render(request, 'department.html', dic_dep)

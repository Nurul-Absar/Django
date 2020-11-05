from django.http import HttpResponse
from django.shortcuts import render

def employee(request):
    return HttpResponse('this is our employee page')
def profile(request):
    return render(request,'employee/profile.html')
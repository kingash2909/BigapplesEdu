from typing import Dict, Any

from django.shortcuts import render
from .models import  CourseName


# Create your views here.

def Python(request):
    smaterials = SMaterials.objects.all()
    return render(request, 'smaterials/study.html', {'smaterials': smaterials}, )


def studymaterials(request):
    coursename = CourseName.objects.all()
    return render(request, 'smaterials/studymaterials.html', {'coursename': coursename})


def search1(request):
    query1 = request.GET.get('query1')
    smaterial = SMaterials.objects.filter(title1__icontains=query1)
    params = {'smaterial': smaterial}
    return render(request, 'smaterials/search1.html', params)

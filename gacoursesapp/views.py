from django.shortcuts import render
from django.http import HttpResponse
from gacoursesapp.models import Course

def index(request):
    context_dict = {}
    context_dict['courses'] = Course.objects.order_by('title')
    return render(request, 'gacoursesapp/index.html', context=context_dict)

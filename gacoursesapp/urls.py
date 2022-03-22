from django.urls import path
from gacoursesapp import views

app_name = 'gacoursesapp'

urlpatterns = [
    path('', views.index, name='index')
]
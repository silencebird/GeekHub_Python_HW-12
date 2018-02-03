from django.urls import path, re_path

from geekhub import views

urlpatterns = [
    path('', views.index, name='home'),
    path('courses/', views.courses, name='courses'),
    path('newstudent/', views.newstudent, name='newstudent'),
]
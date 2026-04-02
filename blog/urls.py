from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    path("create/save", views.save),
    path('', views.list),
]

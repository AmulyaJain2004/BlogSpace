from django.urls import path, include
from myapp import views

urlpatterns = [
    path('home/', views.home),
    path('signup/', views.signup)
]

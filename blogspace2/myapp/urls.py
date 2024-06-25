# from django.urls import path, include
# from myapp import views

# urlpatterns = [
#     path('home/', views.home),
#     path('signup/', views.signup),
#     path('signin/', views.signin),
#     path('contactus/', views.contactus),
#     path('tips/', views.tips),
#     path('getstart/', views.getstart),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup_view),
    path('signin/', views.signin_view),
    path('forgotpwd/', views.forgot_password_view),
    path('contactus/', views.contactus),
    path('tips/', views.tips),
    path('getstart/', views.getstart),
]


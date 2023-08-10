from . import views
from django.urls import path

urlpatterns=[
    path('static_website/', views.static_website, name='static_website'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]

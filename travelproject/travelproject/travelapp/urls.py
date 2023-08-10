from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('passing_value/',views.passing_value,name='passing_value'),
    path('add/',views.addition,name='addition'),
    path('static_website/', views.static_website, name='static_website'),
]


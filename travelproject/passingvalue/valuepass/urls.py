from . import views
from django.urls import path

urlpatterns = [
    path('operations/',views.value,name='operations')
]
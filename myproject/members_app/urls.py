from django.urls import path
from .views import input_view, display_view, session_view

urlpatterns = [
    path('input/', input_view, name='input'),
    path('display/', display_view, name='display'),
    path('session/', session_view, name='session'),
]

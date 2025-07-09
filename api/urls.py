from django.urls import re_path
from .views import BookView, health_view

app_name = 'api'

urlpatterns = [
    re_path(r"^$", health_view, name='health'),
    re_path(r"^books/", BookView.as_view(), name='books'), 
]

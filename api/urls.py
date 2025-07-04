from django.urls import path
from .views import RootView, HealthView, BookView

urlpatterns = [
    path('', RootView.as_view(), name='root'), 
    path('health/', HealthView.as_view(), name='health'),
    path('books/', BookView.as_view(), name='books'),
]

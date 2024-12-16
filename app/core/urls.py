from django.urls import path
from .views import taskview

urlpatterns = [
    path('task/',taskview.as_view())
]
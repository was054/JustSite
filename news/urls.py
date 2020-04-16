from django.urls import path
from .views import index, new, by_rubric

urlpatterns = [
    path('', by_rubric, name='by_rubric'),
    path('new', new, name='NewsIndex'),
]



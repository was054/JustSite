from django.urls import path
from .views import new, by_rubric, index_count

urlpatterns = [
    path('', by_rubric, name='by_rubric'),
    path('new', new, name='NewsIndex'),
    path('counter', index_count, name='counter'),

]




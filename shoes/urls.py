from django.urls import path
from .views import recommend_shoes

urlpatterns = [
    path('', recommend_shoes, name='recommend_shoes'),
]

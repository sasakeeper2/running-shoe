from django.urls import path
from .views import recommend_shoes, login_view, signup_view

urlpatterns = [
    path('recommender', recommend_shoes, name='recommend_shoes'),
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]

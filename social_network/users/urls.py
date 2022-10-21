from django.urls import path
from .views import profile_list, user_profile
urlpatterns = [
    path('profiles/', profile_list),
    path('profile/<int:pk>/', user_profile),
]

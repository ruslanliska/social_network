from django.urls import path
from .views import profile_list, user_profile, posts_list
urlpatterns = [
    path('profiles/', profile_list),
    path('profile/<int:pk>/', user_profile),
    path('posts', posts_list)
]

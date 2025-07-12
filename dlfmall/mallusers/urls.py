from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view()),
    path('userslist/', views.UserListView.as_view()),
]

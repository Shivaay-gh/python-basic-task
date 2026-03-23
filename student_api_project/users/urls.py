from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
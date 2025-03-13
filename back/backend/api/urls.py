from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import TaskList, TaskDetail
from users.views import UserList, UserDetail

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
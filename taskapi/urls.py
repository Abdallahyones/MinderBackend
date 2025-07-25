from django.urls import path
from .views import (
    TaskListCreateView,
    TaskRetrieveDeleteView,
    ImportantTaskListView
)

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),               # GET for get all tasks or POST for create a new task
    path('important/', ImportantTaskListView.as_view(), name='important-tasks'),   # GET for get all important tasks
    path('<int:pk>/', TaskRetrieveDeleteView.as_view(), name='task-detail-delete') # GET a task by id  or DELETE for delete a task by id
]

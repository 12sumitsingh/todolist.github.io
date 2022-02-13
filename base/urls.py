from django.urls import path
from . import views

urlpatterns = [

    path('', views.taskList, name="task-list"),
    path('taskview/<str:pk>/', views.taskView, name="taskview"),
    path('createtask/', views.createTask, name="createtask"),
    path('updatetask/<str:pk>/', views.updateTask, name="updatetask"),
    path('deletetask/<int:pk>/', views.deleteTask, name="deletetask"),
    path('login/', views.Loginuser, name="login"),
    path('logout/', views.Logoutuser, name="logout"),
    path('register/', views.registeruser , name="register"),

]
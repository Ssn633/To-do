from django.urls import path
from .views import RegisterPage,TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CoustemLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CoustemLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',TaskList.as_view(),name='task'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('create_task/',TaskCreate.as_view(),name='task-create'),
    path('update_task/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('delete_task/<int:pk>',DeleteView.as_view(),name='task-delete'),
]


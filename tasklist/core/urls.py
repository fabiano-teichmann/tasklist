from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create', views.CreateTaskListView.as_view(), name='create'),
    path('edit/<slug:slug>', views.EditTaskListView.as_view(), name='edit'),
    path('delete/<slug:slug>', views.DeleteTaskListView.as_view(), name='delete'),

]

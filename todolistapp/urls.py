from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name="create"),
    path('store', views.store, name="store"),
    path('edit/<str:todo_id>/', views.edit, name="edit"),
    path('update/<str:todo_id>', views.update, name="update"),
    path('delete/<str:todo_id>', views.delete, name="delete")
]

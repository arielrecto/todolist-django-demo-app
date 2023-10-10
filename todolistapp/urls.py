from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.signup, name="register"),
    path('store_user', views.store_user, name="store_user"),
    path('login/', views.signin, name="login"),
    path('auth_user', views.auth_user, name="auth_user"),
    path('logout', views.signoff, name="signoff"),
    path('create/', views.create, name="create"),
    path('store', views.store, name="store"),
    path('edit/<str:todo_id>/', views.edit, name="edit"),
    path('update/<str:todo_id>', views.update, name="update"),
    path('delete/<str:todo_id>', views.delete, name="delete")
]

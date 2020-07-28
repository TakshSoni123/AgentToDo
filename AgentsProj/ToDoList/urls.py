from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('showagentsAPI', views.showagents, name='show'),
    path('login', views.login),
    path('showtodoAPI', views.showTodo, name='showtodo'),
    path('todo', views.todoView),
]
from django.urls import path
from . import views

app_name = 'webtext'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('<int:pk>/home/', views.UserHomeView.as_view(), name='userHome'),
    path('<int:user_id>/new_message/', views.new_message, name='new_message')
]
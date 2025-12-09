from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('chat/', views.chat_api, name='chat_api'),
    path('logout/', views.logout_view, name='logout'),
]

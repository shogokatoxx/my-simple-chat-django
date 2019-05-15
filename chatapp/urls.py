from django.urls import path
from . import views

urlpatterns = [
    path('',views.top,name='top'),
    path('chat/<int:pk>',views.chat,name='chat'),
    path('seach',views.seach,name='seach'),
]

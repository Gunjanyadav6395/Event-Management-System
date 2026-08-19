from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test_gemini, name="test_gemini"),
    path("chat/", views.chat_with_gemini, name="chat_with_gemini"),
]
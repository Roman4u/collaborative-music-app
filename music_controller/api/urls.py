from django.urls import path
from .views import RoomView

urlpatterns = [
    # second api endpoint
    path('room', RoomView.as_view()),
]
from django.urls import path
from .views import RoomView

urlpatterns = [
    # second api endpoint
    path('home', RoomView.as_view()),
]
from django.urls import path
from .views import VideoStreamingView

urlpatterns = [
    path('', VideoStreamingView.as_view(), name='video_streaming_home'),
]
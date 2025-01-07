from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gaming/', include('gaming.urls')),
    path('video_streaming/', include('video_streaming.urls')),
]
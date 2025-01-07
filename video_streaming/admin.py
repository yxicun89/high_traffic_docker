from django.contrib import admin
from .models import Video  # Assuming you have a Video model in models.py

admin.site.register(Video)  # Register the Video model with the admin site
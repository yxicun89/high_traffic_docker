from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class VideoStreamingView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return JsonResponse({"message": "Welcome to the Video Streaming Service!"})

    def post(self, request):
        # Logic for handling video streaming requests can be added here
        return JsonResponse({"message": "Video streaming request received."})
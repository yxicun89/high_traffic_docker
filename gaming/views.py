from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Game
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class GamingView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get(self, request):
        # Logic to handle GET requests for gaming
        return JsonResponse({'message': 'Welcome to the Gaming section!'})

    def post(self, request):
        # Logic to handle POST requests for gaming
        return JsonResponse({'message': 'Gaming data received!'}, status=201)

class GameListView(ListView):
    model = Game
    template_name = 'gaming/game_list.html'

class GameDetailView(DetailView):
    model = Game
    template_name = 'gaming/game_detail.html'


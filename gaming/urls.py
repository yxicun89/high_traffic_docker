# from django.urls import path
# from .views import GameListView, GameDetailView

# urlpatterns = [
#     path('', GameListView.as_view(), name='game_list'),
#     path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),
# ]

# from django.urls import path
# from .views import GameListView, GameDetailView, GamingView

# urlpatterns = [
#     path('', GameListView.as_view(), name='game_list'),
#     path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),
#     path('gaming/', GamingView.as_view(), name='gaming_home'),
# ]

from django.urls import path
from .views import GameListView, GameDetailView, GamingView

urlpatterns = [
    path('', GamingView.as_view(), name='gaming_home'),
    path('list/', GameListView.as_view(), name='game_list'),
    path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),
]
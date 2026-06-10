"""
Hindi Land API urls
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

router = DefaultRouter()
router.register(r'players', views.PlayerViewSet, basename='player')
router.register(r'matches', views.MatchViewSet, basename='match')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('health/', views.HealthCheckView.as_view(), name='health'),
]

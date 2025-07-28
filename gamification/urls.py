from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, PointViewSet, LevelViewSet, BadgeViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'points', PointViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'badges', BadgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
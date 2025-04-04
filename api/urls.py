from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, OfferViewSet, WeDoSerializer, ChooseUsSerializer , CustomServicesSerializer, WeWorkSerializer, NewsSerializer

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'wedos', WeDoSerializer, basename='wedo')
router.register(r'chooseus', ChooseUsSerializer, basename='chooseus')
router.register(r'customservices', CustomServicesSerializer, basename='customservices')
router.register(r'wework', WeWorkSerializer, basename='wework')
router.register(r'news', NewsSerializer, basename='news')

# Include router.urls in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # This is necessary for DRF to work
]

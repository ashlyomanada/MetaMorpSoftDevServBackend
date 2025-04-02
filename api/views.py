from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .models import Offer
from .serializers import TaskSerializer
from .serializers import OfferSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer
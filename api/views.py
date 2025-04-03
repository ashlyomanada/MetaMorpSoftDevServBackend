from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .models import Offer
from .models import WeDo
from .models import ChooseUs
from .serializers import TaskSerializer
from .serializers import OfferSerializer
from .serializers import WeDoSerializer
from .serializers import ChooseUsSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer

class WeDoSerializer(viewsets.ModelViewSet):
    queryset = WeDo.objects.all().order_by('-id')
    serializer_class = WeDoSerializer

class ChooseUsSerializer(viewsets.ModelViewSet):
    queryset = ChooseUs.objects.all().order_by('-id')
    serializer_class = ChooseUsSerializer
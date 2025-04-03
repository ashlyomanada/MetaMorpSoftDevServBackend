from rest_framework import serializers
from .models import Task
from .models import Offer
from .models import WeDo
from .models import ChooseUs

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class WeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeDo
        fields = '__all__'

class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = '__all__'
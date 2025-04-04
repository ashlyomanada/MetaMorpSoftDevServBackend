from rest_framework import serializers
from .models import Task
from .models import Offer
from .models import WeDo
from .models import ChooseUs
from .models import CustomServices
from .models import WeWork
from .models import News

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

class CustomServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomServices
        fields = '__all__'

class WeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeWork
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
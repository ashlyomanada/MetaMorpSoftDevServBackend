from rest_framework import serializers
from .models import Task
from .models import Offer
from .models import WeDo
from .models import ChooseUs
from .models import CustomServices
from .models import WeWork
from .models import TechWeUse
from .models import News
from .models import WebActivities
from .models import WhyMeta
from .models import HowWeDo

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

class TechWeUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechWeUse
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class WebActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebActivities
        fields = '__all__'

class WhyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyMeta
        fields = '__all__'

class HowWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeDo
        fields = '__all__'
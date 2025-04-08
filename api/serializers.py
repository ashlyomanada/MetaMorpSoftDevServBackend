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
from .models import CaseStudies
from .models import AboutUxUi
from .models import OurUxUi
from .models import UxServices
from .models import UiServices
from .models import QaAbout
from .models import QaWhyMeta
from .models import QaHowWeDo
from .models import QaTesting
from .models import CloudOffer
from .models import CloudBenefits
from .models import WhoWeAre
from .models import MissionVission
from .models import CompanyCulture
from .models import ManageTeam
from .models import BusPhilosophy
from .models import HowWeWork
from .models import DevelopmentStage
from .models import AchieveSuccess
from .models import WhyChooseUs
from .models import Partnership
from .models import PartnershipDropDowns

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
        
class CaseStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudies
        fields = '__all__'

class AboutUxUiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUxUi
        fields = '__all__'

class OurUxUiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUxUi
        fields = '__all__'

class UxServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UxServices
        fields = '__all__'

class UiServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UiServices
        fields = '__all__'

class QaAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaAbout
        fields = '__all__'

class QaWhyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaWhyMeta
        fields = '__all__'

class QaHowWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaHowWeDo
        fields = '__all__'

class QaTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QaTesting
        fields = '__all__'

class CloudOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudOffer
        fields = '__all__'

class CloudBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudBenefits
        fields = '__all__'

class WhoWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoWeAre
        fields = '__all__'

class MissionVissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVission
        fields = '__all__'

class CompanyCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCulture
        fields = '__all__'

class ManageTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageTeam
        fields = '__all__'

class BusPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusPhilosophy
        fields = '__all__'

class HowWeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWork
        fields = '__all__'

class DevelopmentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class AchieveSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveSuccess
        fields = '__all__'

class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'
        
class PartnershipDropDownsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipDropDowns
        fields = '__all__'

        